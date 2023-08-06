import copy
from datetime import datetime, timedelta
from functools import wraps


class UnSupportedDataTypeException(Exception):
    pass


class Cache:
    _cache = []

    def __init__(self, hours=None, minutes=None, seconds=None):
        self._time = 0

        if hours is not None:
            self._time += hours * 60 * 60

        if minutes is not None:
            self._time += minutes * 60

        if seconds is not None:
            self._time += seconds

    def __call__(self, *param_arg, **param_kwargs):
        @wraps(param_arg[0])
        def wrapper(ctx, *args, **kwargs):
            key = self._get_key(param_arg[0], *args, **kwargs)
            result = self.__get_data(key)

            if result is None:
                result = param_arg[0](ctx, *args, **kwargs)

                self.__add(key, result)

            return result

        return wrapper

    @staticmethod
    def _get_key(func, *args, **kwargs) -> str:
        key_args = [str(arg) for arg in args]
        key_kwargs = []

        for key, value in kwargs.items():
            key_kwargs.append(f"{key}={value}")

        return f"{func.__name__}/{'/'.join(key_args)}/{'/'.join(key_kwargs)}"

    def __add(self, key, data):
        self._cache.append({
            "expire": datetime.now() + timedelta(seconds=self._time),
            "key": key,
            "data": copy.deepcopy(data)
        })

    def __get(self, key):
        for item in self._cache:
            if item["key"] == key:
                return item

        return None

    def __get_data(self, key):
        cache = self.__get(key)

        if cache is None:
            return None

        if cache["expire"] < datetime.now():
            self._cache.remove(cache)

            return None

        return cache["data"]
