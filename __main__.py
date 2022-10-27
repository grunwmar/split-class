from splitclass import SplitClass


class Vector(metaclass=SplitClass):
    """ Class representing arithmetic vector """

    parts: ['vector.operations', 'vector.special']

    def __init__(self, *elements):
        self._elements = elements

    @property
    def tuple(self):
        return self._elements

    def __str__(self):
        r = repr(self.tuple)
        return f'{self.__class__.__name__}{r}'


# Examples of operations

x = Vector(1, 0, 0)
y = Vector(0, 1, 0)
z = Vector(0, 0, 1)
print(f" > Vectors: x = {x}, y = {y}, z = {z}\n")

n1 = x.norm
n2 = y.norm
n3 = z.norm
print(f""" > Norm:
    {x}.norm = {n1}
    {y}.norm = {n2}
    {z}.norm = {n3}
""")


u = x + y + z
print(f" > Sum: {x} + {y} + {z} = {u}\n")

s1 = x @ y
s2 = x @ z
s3 = y @ z
print(f""" > Scalar products:
    {x} @ {y} = {s1}
    {x} @ {z} = {s2}
    {y} @ {z} = {s3}
""")

v1 = x ^ y
v2 = x ^ z
v3 = y ^ z
print(f""" > Vector products:
    {x} ^ {y} = {v1}
    {x} ^ {z} = {v2}
    {y} ^ {z} = {v3}
""")
