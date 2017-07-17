from __future__ import print_function, unicode_literals

from uscensus.errors import *


def CensusError_test():
    e = CensusError("test")
    assert isinstance(e, Exception)


def DBError_test():
    e = DBError("test")
    assert isinstance(e, CensusError)
    assert isinstance(e, Exception)
