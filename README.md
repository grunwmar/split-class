# split-class

Option for classes to be divided in more files.

```python
from spliclass import splitclass

@splitclass
class MyClass:

  #class definition
  ...
  
```
Usage of decorator @splitclass will search for directory `./@MyClass` and tries to import files contained in it as python modules in which searches for classes named `MyClass`
having attribute `__partial__ = True`. Then updates `__dict__` of such partial class to its original `__dict__` and creates 'itself' de novo using `type()` constructor.

**`./@MyClass/some_filename.py`**
```python
from splitclass import partialclass

@partialclass
class MyClass:

  # extended class definition
  ...
 
```

Partial class is marked by decorator `@partialclass` which adds an attribute `__partial__ = True` to its body.
