#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue September 12 00:24:09 2023

@author Nzeamalu Chikelue
"""


class MyList(list):
    """
     class MyList that inherits from list
    """
    def print_sorted(self):
        """
        Public instance method that prints sorted list
        """
        list_copy = self[:]
        list_copy.sort()
        print(list_copy)
