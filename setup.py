from setuptools import setup

setup(
    name="rdrf-mixin-cache",
    description="Easy to use cache framework for django-rest-framwork apps",
    keywords="drf, django, rest, framework, cache",
    url="https://github.com/null-none/drf-mixin-cache",
    packages=[
        "rest_framework_cache",
    ],
    namespace_packages=["drf_mixin_cache"],
    package_dir={"drf_mixin_cache": "drf_mixin_cache"},
    classifiers=["Framework :: Django"],
)
