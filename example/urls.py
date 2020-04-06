from django.conf.urls import include, url
from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    url(r"oauth/", include("iitb_oauth.urls")),
]
