from __future__ import absolute_import

from .data_descriptor import IDataDescriptor
from dynd import nd, ndt

def dd_as_py(dd):
    """
    Converts the data in a data descriptor into Python
    types. This uses the data_descriptor iteration methods,
    so is not expected to be fast. Its main initial purpose
    is to assist with writing unit tests.
    """
    # TODO: This function should probably be removed.
    if not isinstance(dd, IDataDescriptor):
        raise TypeError('expected DataDescriptor, got %r' % type(dd))
    if not dd.is_concrete:
        from .. import Array, eval
        dd = eval(Array(dd))._data
    return nd.as_py(dd.dynd_arr())
