""" Class which allow to split its content into multiple files. """

import importlib
import types


class PartialClass:
    """ Rises TypeError in case of atempt to instantiate it."""

    def __init__(mcs, *args, **kwargs):
        raise TypeError('PartialClass cannot be instantiated.')


class SplitClass(type):
    """ Metaclass allowing to split child class to multiple files """

    def __call__(mcs, *args, **kwargs):

        # reads modules containing SplitClass parts
        partial_classes = mcs.__annotations__['parts']

        new_attributes = {}

        for part in partial_classes:

            # loading found classes parts
            part_module = importlib.import_module(f'{part}')
            part_class = part_module.__dict__[mcs.__name__]

            # raise TypeError if found class does not inherits from SplitClass
            if not PartialClass in part_class.__bases__:
                raise TypeError(f'Class {part}.{part_class.__name__} does not inherits from PartialClass.')

            # collected new attributes from valid partial classes
            for k, v in part_class.__dict__.items():
                new_attributes[k] = v


        # updates collected attributes to original attributes
        original_attributes = new_attributes
        original_attributes.update(mcs.__dict__)

        # creates new class with all collected attributes merged to attributes
        # of original class
        new_class = type(mcs.__name__, mcs.__bases__, original_attributes)(*args, **kwargs)

        return new_class
