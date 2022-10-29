from splitclass import partialclass
import math

@partialclass
class Vector():
    """ Part of Vector class containing definitions """
    """ of more advanced vector operations """

    def __matmul__(self, other):
        z = zip(self.tuple, other.tuple)
        elements = [ x * y for x,y in z ]
        return sum(elements)


    def __xor__(self, other):
        if len(self.tuple) != 3 or len(self.tuple) != 3:
            raise ValueError('Vector must have a dimension equal to 3.')

        a1, a2, a3 = self.tuple
        b1, b2, b3 = other.tuple

        c1 = a2*b3 - a3*b2
        c2 = a3*b1 - a1*b3
        c3 = a1*b2 - a2*b1

        return self.__class__(c1, c2, c3)

    @property
    def norm(self):
        return math.sqrt(sum([ x ** 2 for x in self.tuple ]))
