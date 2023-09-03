#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun September 03 17:16:59 2023

@author Nzeamalu Chikelue
"""
from numpy import matmul


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrix

    Args:
        m_a (list): First matrix
        m_b (list): second matrix

    Returns:
        The result of multiply m_a by m_b

    """
    return matmul(m_a, m_b)
