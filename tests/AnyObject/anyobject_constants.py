import sys
sys.path.append('../../../split-class')

from splitclass import partialclass


@partialclass
class AnyObject:

    CONSTANT = '1234567890'
