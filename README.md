# drf-mixin-cache

Easy to use cache framework for django-rest-framwork apps.


# Installation

Install using `pip`...

    pip install drf_mixin_cache

Add `'drf_mixin_cache'` to your `INSTALLED_APPS` setting.

```python
INSTALLED_APPS = (
    ...
    'drf_mixin_cache',
)
```

You must execute autodiscover to load your serializers. To do this change your `urls.py` adding the following code:

```python
from drf_mixin_cache.registry import cache_registry

cache_registry.autodiscover()
```


# Usage

```python
from rest_framework import serializers

# You must import the CachedSerializerMixin and cache_registry
from rest_framework_cache.serializers import CachedSerializerMixin
from rest_framework_cache.registry import cache_registry

from .models import User


class UserSerializer(serializers.ModelSerializer, CachedSerializerMixin):

    class Meta:
        model = User


cache_registry.register(UserSerializer)

```


## Using cache backend different of the default

If you need use a cache backend different of the default you can specify it on the `REST_FRAMEWORK_CACHE`.

To do this edit your `settings.py` like this:

```python
# ...
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    },
    'locmem': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

REST_FRAMEWORK_CACHE = {
    'DEFAULT_CACHE_BACKEND': 'locmem',
}
# ...
```

## Cache timeout

You can set the cache timeout using `DEFAULT_CACHE_TIMEOUT`.

```python
REST_FRAMEWORK_CACHE = {
    'DEFAULT_CACHE_TIMEOUT': 86400, # Default is 1 day
}

```
