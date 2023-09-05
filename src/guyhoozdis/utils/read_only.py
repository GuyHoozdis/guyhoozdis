from __future__ import annotations

from types import MappingProxyType


# TODO: Just dropping this here to get the idea started.
# - Maybe make as a decorator that applies this to the return value of a function.
# - Maybe extend this to work on lists too.  Could still use the proxies from Mappings to work for a list.
def read_only(mapping: Mapping) -> MappingProxyType:
    def walk(mapping):
        for key, value in mapping.items():
            if not isinstance(value, Mapping):
                yield (key, value)
            else:
                sub_mapping = {k: v for k, v in walk(value)}
                yield (key, MappingProxyType(sub_mapping))

    return MappingProxyType({k: v for k, v in walk(mapping)})

