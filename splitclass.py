""" Class which allow to split its content into multiple files. """
import os
import importlib
import types


def _raise_cannot_instantiate(*args):
    raise TypeError(f"Creating an instance of {args[0]} is not permitted.")
    ...


def partialclass(cls):
    """ Marks class as partial """

    new_attrs = dict(cls.__dict__)
    new_attrs.update(
        {
            "__partial__": True,
            "__call__": _raise_cannot_instantiate
        }
    )

    new_class = type(
                    cls.__name__,
                    cls.__bases__,
                    new_attrs
                )

    return new_class


def splitclass(cls):
    """ Decorator allowing to split child class to multiple files """

    new_attributes = {}

    if (hasattr(cls, '__annotations__') and
                        cls.__annotations__.get('partials') is not None):

        for part in cls.__annotations__.get('partials'):

            # loading found classes parts
            part_module = importlib.import_module(f"{part}")
            part_class = part_module.__dict__[cls.__name__]

            if not part_class.__partial__ == True:
                raise TypeError(f"Class {part_class} is not a partial class.")

            # collected new attributes from valid partial classes
            for k, v in part_class.__dict__.items():
                if k in ["__partial__"]:
                    continue
                new_attributes[k] = v

    # updates collected attributes to original attributes
    original_attributes = new_attributes
    original_attributes.update(cls.__dict__)

    # creates new class with all collected attributes merged to attributes
    # of original class
    new_class = type(cls.__name__, cls.__bases__, original_attributes)

    return new_class
