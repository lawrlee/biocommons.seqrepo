import gzip
import io

import six

if six.PY2:

    from .lru_cache import lru_cache
    from .makedirs import makedirs
    from .commonpath import commonpath

    def gzip_open_encoded(file, encoding=None):
        return io.TextIOWrapper(io.BufferedReader(gzip.open(file)), encoding="utf8")

else:

    from os import makedirs     # flake8: noqa
    from os.path import commonpath
    from functools import lru_cache

    def gzip_open_encoded(file, encoding=None):
        return gzip.open(file, mode="rt", encoding=encoding)
