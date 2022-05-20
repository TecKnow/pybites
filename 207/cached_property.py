from random import random
from time import sleep

from attr import Attribute


def cached_property(func):
    def setter(self, value):
        raise AttributeError()
    return property(func, setter)


class Planet:
    """the nicest little orb this side of Orion's Belt"""

    GRAVITY_CONSTANT = 42
    TEMPORAL_SHIFT = 0.12345
    SOLAR_MASS_UNITS = 'M\N{SUN}'

    def __init__(self, color):
        self.color = color
        self._mass = None

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.color)})'

    @cached_property
    def mass(self):
        if (precomputed_mass := getattr(self, "_mass")) is not None:
            return precomputed_mass
        else:
            scale_factor = random()
            sleep(self.TEMPORAL_SHIFT)
            self._mass = (f'{round(scale_factor * self.GRAVITY_CONSTANT, 4)} '
                          f'{self.SOLAR_MASS_UNITS}')
            return self._mass
