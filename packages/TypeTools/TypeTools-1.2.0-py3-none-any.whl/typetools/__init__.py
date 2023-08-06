from ._descriptor import Descriptor
from ._typed import Typed
from ._broadtypes import *
from ._types import Integer, Float, String, List, Mapping


def checkattrs(**kwargs):
    def decorator(cls):
        for k, v in kwargs.items():
            if isinstance(v, Descriptor):
                v.name = k
                setattr(cls, k, v)
            else:
                setattr(cls, k, v(k))
        return cls

    return decorator
