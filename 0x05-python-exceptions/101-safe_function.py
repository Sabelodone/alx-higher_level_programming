#!/usr/bin/python3
from __future__ import print_function
import sys

def safe_function(function, *args):
    try:
        result = function(*args)
    except Exception as exception:
        print("Exception: {}".format(exception), file=sys.stderr)
        return None
    else:
        return result
