from django.conf import settings


def get_django_setting_or_default(setting_name, default):
    """
    Wrapper for checking if something exists in the settings or not. Return the default otherwise
    @param setting_name: the key of the config value
    @param default: the default value to get otherwise
    @return: whatever datatype you hoped to get from the settings
    """
    if hasattr(settings, setting_name) and getattr(settings, setting_name):
        return getattr(settings, setting_name)
    else:
        return default


def check_key_and_get(my_dict, key):
    if key is None:
        raise ValueError("key must be specified")
    if key in my_dict:
        return my_dict[key]
    return ""
