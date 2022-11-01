import sys
sys.path.append('../../../split-class')

from splitclass import partialclass


@partialclass
class Vector():
    """ Part of Vector class containing definitions of basic vecor operations """

    def __add__(self, other):
        z = zip(self.tuple, other.tuple)
        return self.__class__(*(x + y for x, y in z))


    def __sub__(self, other):
        z = zip(self.tuple, other.tuple)
        return self.__class__(*(x - y for x, y in z))


    def __rmul__(self, number):
        return self.__class__(*(number * x for x in self.tuple))


    def __truediv__(self, number):
        return self.__class__(*(x / number for x in self.tuple))
