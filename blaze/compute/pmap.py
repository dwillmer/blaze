from __future__ import absolute_import, division, print_function

default_map = [map]

def set_default_pmap(func):
    default_map[0] = func


def get_default_pmap():
    return default_map[0]
