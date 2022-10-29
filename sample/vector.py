
import sys
sys.path.append('../../split-class')

from splitclass import splitclass


@splitclass
class Vector:
    """ Class representing arithmetic vector """

    def __init__(self, *elements):
        self._elements = elements

    @property
    def tuple(self):
        return self._elements

    def __str__(self):
        r = repr(self.tuple)
        return f'{self.__class__.__name__}{r}'
