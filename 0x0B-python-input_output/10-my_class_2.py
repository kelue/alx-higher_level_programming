#!/usr/bin/python3
""" My class module
"""
Created on Fri September 15 19:52:47 2023

@author Nzeamalu Chikelue
"""
    """
    score = 0

    def __init__(self, name, number=4):
        self.__name = name
        self.number = number
        self.is_team_red = (self.number % 2) == 0

    def win(self):
        self.score += 1

    def lose(self):
        self.score -= 1

    def __str__(self):
        return "[MyClass] {} - {:d} => {:d}"\
                .format(self.__name, self.number, self.score)
