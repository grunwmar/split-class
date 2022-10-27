from splitclass import PartialClass


class Vector(PartialClass):
    """ Part of Vector class containing definitions of basic vecor operations """

    def __add__(self, other):
        z = zip(self.tuple, other.tuple)
        elements = [ x + y for x,y in z ]
        return self.__class__(*elements)


    def __sub__(self, other):
        z = zip(self.tuple, other.tuple)
        elements = [ x - y for x,y in z ]
        return self.__class__(*elements)


    def __rmul__(self, number):
        elements = [ number * x for x in self.tuple ]
        return self.__class__(*elements)


    def __truediv__(self, number):
        elements = [ x / number for x in self.tuple ]
        return self.__class__(*elements)
