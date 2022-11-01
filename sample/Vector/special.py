import sys
sys.path.append('../../../split-class')

from splitclass import partialclass
import math

@partialclass
class Vector():
    """ Part of Vector class containing definitions """
    """ of more advanced vector operations """

    def __matmul__(self, other):
        z = zip(self.tuple, other.tuple)
        return sum(x * y for x, y in z)


    def __xor__(self, other):
        """ Cross product in common sense of two vectors is valid only in """
        """ 3-dimensional space. Although it could be meaningful to have """
        """ definition also for 2-dimensinal space. """
        """ For that case the 2-D vectors are understood as 3-D vectors with """
        """ 3rd elements equal to zero."""
        """ Because the result of cross product is vector perpendicular """
        """ to both input vectors, which cannot be realised in 2-D space, """
        """ the return value is just  a norm of that non-existing """
        """ hypothetical vector multiplied by its direction. """

        if len(self.tuple) == 3 and len(other.tuple) == 3:
            a1, a2, a3 = self.tuple
            b1, b2, b3 = other.tuple

            c1 = a2*b3 - a3*b2
            c2 = a3*b1 - a1*b3
            c3 = a1*b2 - a2*b1

            return self.__class__(c1, c2, c3)

        elif len(self.tuple) == 2 and len(other.tuple) == 2:
            a1, a2 = self.tuple
            b1, b2 = other.tuple

            return a1*b2 - a2*b1

        else:
            raise ValueError("Both vector has to have same size. Size must be 2 or 3.")

    @property
    def norm(self):
        """ Eucleidian norm is defined as square root of scalar product """
        """ of vector with itself. """

        return math.sqrt(self @ self)
