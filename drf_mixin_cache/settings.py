from __future__ import unicode_literals

from django.conf import settings
from django.test.signals import setting_changed


DEFAULTS = {
    "DEFAULT_CACHE_BACKEND": "default",
    "DEFAULT_CACHE_TIMEOUT": 86400,
    "SERIALIZER_CACHE_KEY_FORMAT": "{protocol}.{app_label}.{model_name}."
    "{serializer_name}:{id}",
}


class APISettings(object):
    def __init__(self, defaults=None):
        self.defaults = defaults
        self.settings = getattr(settings, "REST_FRAMEWORK_CACHE", {})

    def __getattr__(self, attr):
        if attr not in self.defaults:
            raise AttributeError("Invalid API setting: '%s'" % attr)

        try:
            val = self.settings[attr]
        except KeyError:
            val = self.defaults[attr]

        return val


api_settings = APISettings(DEFAULTS)


def reload_api_settings(*args, **kwargs):
    global api_settings
    setting, value = kwargs["setting"], kwargs["value"]
    if setting == "REST_FRAMEWORK_CACHE":
        api_settings = APISettings(DEFAULTS)


setting_changed.connect(reload_api_settings)
