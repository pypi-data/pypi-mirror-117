[![PyPI version](https://badge.fury.io/py/OutCache.svg)](https://pypi.org/project/OutCache)
# OutCache
Function output cacher

Usage:

```python
from outcache import Cache


@Cache(minutes=1)
def get_profile(email: str, username: str):
    my_dict = {"email": email, "username": username}

    return my_dict


profile = get_profile("example@example.com", username="example")
```