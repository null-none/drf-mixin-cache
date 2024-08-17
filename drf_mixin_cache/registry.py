from django.db.models import signals
from django.utils.module_loading import autodiscover_modules

from .exceptions import AlreadyRegistered


class CacheRegistry:

    def __init__(self):
        self._registry = {}

    def register(self, serializer):
        model = serializer.Meta.model

        if model not in self._registry:
            self._registry[model] = []

        if serializer in self._registry[model]:
            raise AlreadyRegistered(
                "Serializer {} is already registered".format(model.__name__)
            )

        self._registry[model].append(serializer)
        self.connect_signals(model)

    def connect_signals(self, model):
        from .signals import clear_instance  # NOQA - Prevent circular import

        signals.post_save.connect(clear_instance, sender=model)
        signals.pre_delete.connect(clear_instance, sender=model)

    def get(self, model):
        return self._registry.get(model, [])

    def autodiscover(self):
        autodiscover_modules("serializers")


cache_registry = CacheRegistry()
