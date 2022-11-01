import sys
sys.path.append('../../../split-class')

from splitclass import partialclass


@partialclass
class AnyObject:

    def any_method(self):
        return f"Hello {self.name}"
