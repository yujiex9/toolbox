import functools
import math
import operator
import reprlib
from array import array


# compatible with version < 3.8
def singledispatchmethod_(func):
    dispatcher = functools.singledispatch(func)
    def wrapper(*args, **kwargs):
        return dispatcher.dispatch(args[1].__class__)(*args, **kwargs)
    wrapper.register = dispatcher.register
    functools.update_wrapper(wrapper, dispatcher)
    return wrapper


if not hasattr(functools, 'singledispatchmethod'):
    singledispatchmethod = singledispatchmethod_
else:
    singledispatchmethod = functools.singledispatchmethod


class Vector_:
    typecode = 'd'

    def __init__(self, components):
        self.__components = array(self.typecode, components)

    def __iter__(self):
        return iter(self.components)

    @property
    def components(self):
        return self.__components

    # def __eq__(self, other):
    #     return tuple(self) == tuple(other)
    def __eq__(self, other):
        return (len(self) == len(other) and
                all(a == b for a, b in zip(self, other)))

    def __hash__(self):
        hashes = (hash(item) for item in self)
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return not all(x == 0 for x in self)

    def __len__(self):
        return len(self.components)

    def __getitem__(self, index):
        return self.components[index]

    shortcut_names = 'xyz'

    def __getattr__(self, name):
        cls = self.__class__
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self.components):
                return self.components[pos]
        msg = fr'{cls.__name__} object has no attribute {name}'
        raise AttributeError(msg)


class Vector(Vector_):
    def __repr__(self):
        components = reprlib.repr(self.components)
        components = components[components.find('['):-1]
        return f'{self.__class__.__name__}({components})'
    
    def __str__(self):
        return str(tuple(self))

    @singledispatchmethod
    def __add__(self, other):
        raise NotImplemented

    @__add__.register(Vector_)
    def _(self, other):
        return self.__class__(sum(items) for items in zip(self.components, other.components))

    @__add__.register
    def _(self, other: float):
        return self.__class__(item + other for item in self.components)
