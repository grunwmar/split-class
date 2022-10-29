""" Class which allow to split its content into multiple files. """
import os
import importlib
import types


def _raise_cannot_instantiate(*args):
    raise TypeError(f"Creating an instance of {args[0]} is not permitted.")
    ...


def partialclass(cls):
    """ Marks class as partial """

    def inner():
        cls.__partial__ = True
        setattr(cls, '__call__', _raise_cannot_instantiate)
        return cls
    return inner()


def splitclass(csl):
    """ Decorator allowing to split child class to multiple files """

    def inner():

        dir_name = f"@{csl.__name__}"

        if not os.path.isdir(dir_name):
            os.mkdir(dir_name)

        partial_classes = []

        # reads modules containing SplitClass parts
        for entry in os.listdir(dir_name):
            if os.path.isfile(os.path.join(dir_name, entry)):
                entry, _ = os.path.splitext(entry)
                partial_classes += [f"{dir_name}.{entry}"]

        new_attributes = {}

        for part in partial_classes:

            # loading found classes parts
            part_module = importlib.import_module(f'{part}')
            part_class = part_module.__dict__[csl.__name__]

            if not part_class.__partial__ == True:
                raise TypeError(f"Class {part_class} is not a partial class.")

            # collected new attributes from valid partial classes
            for k, v in part_class.__dict__.items():
                if k in ["__partial__"]:
                    continue
                new_attributes[k] = v

        # updates collected attributes to original attributes
        original_attributes = new_attributes
        original_attributes.update(csl.__dict__)

        # creates new class with all collected attributes merged to attributes
        # of original class
        new_class = type(csl.__name__, csl.__bases__, original_attributes)

        return new_class
    return inner()
