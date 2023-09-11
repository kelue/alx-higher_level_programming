#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue September 12 00:24:09 2023

@author Nzeamalu Chikelue
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if object is an instance of class, or if the object is an instance\
        of a class that inherited from
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class type must be type")
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False
