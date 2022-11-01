# split-class

Option for classes to be divided in more files.

```python
from spliclass import splitclass

@splitclass(partials=['partial.class1', 'partial.class2', ...])
class MyClass:

  #class definition
  ...

```
Use of decorator `@splitclass` will import modules in its parameter `partials=[...]` and check if has class with the same name and if that class has attribute `__partial__ = True`. Then updates `__dict__` of such partial class to its original `__dict__` and creates 'itself' de novo using `type()` constructor.

### `./partial/class1.py`
```python
from splitclass import partialclass

@partialclass
class MyClass:

  # extended class definition
  ...

```

Partial class is marked by decorator `@partialclass` which adds an attribute `__partial__ = True` to its body.
