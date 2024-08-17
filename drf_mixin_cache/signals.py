from .utils import clear_for_instance


def clear_instance(sender, instance, **kwargs):
    clear_for_instance(instance)
