#!/usr/bin/env python3
""" a simple helper function """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ a funtion that returns a tuple of size two containing
        a start index and an end index corresponding to the ranges
        of indexes returned in a list"""
    mul = page - 1
    start = mul * page_size
    stop = start + page_size
    return (start, stop)
