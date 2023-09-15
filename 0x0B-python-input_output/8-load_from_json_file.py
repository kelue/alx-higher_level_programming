#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri September 15 19:52:47 2023

@author Nzeamalu Chikelue
"""
import json


def load_from_json_file(filename):
    """
    Loads an object from json file

    Arguments:
        filename (str): The name of the output file

    Return:
        A file with a text in jason format
    """
    with open(filename, encoding='utf-8') as file:
        return (json.loads(file.read()))
