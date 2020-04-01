from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods

from iitb_oauth.helpers import get_django_setting_or_default


def redirect_to_login(request):
    auth_url = "https://gymkhana.iitb.ac.in/sso/oauth/authorize/"
    client_id = settings.CLIENT_ID
    scope = get_django_setting_or_default("SCOPE", "")
    redirect_uri = settings.REDIRECT_URI
    url = "{}?client_id={}&response_type=code&scope={}&redirect_uri={}".format(
        auth_url, client_id, scope, redirect_uri
    )
    return redirect(url)


@require_http_methods(["GET"])
def authenticate_code(request):
    code = request.GET.get("code")
    user = authenticate(request=request, code=code)
    if user:
        login(request, user)
        if "next" in request.session and request.session["next"]:
            redir_url = request.session["next"]
            del request.session["next"]
            return redirect(redir_url)

        login_complete_redirect = get_django_setting_or_default(
            "LOGIN_COMPLETE_REDIRECT", "/"
        )
        return redirect(login_complete_redirect)
    else:
        # ("Not logged in, redirecting")
        fallback_login = get_django_setting_or_default("FALLBACK_URL", "/")
        return redirect(fallback_login)


def client_logout(req):
    logout(req)
    return redirect(get_django_setting_or_default("LOGOUT_REDIRECT", "/"))
