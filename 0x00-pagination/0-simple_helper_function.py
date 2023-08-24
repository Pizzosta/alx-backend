#!/usr/bin/env python3
""" Contains definition of index_range helper function """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices for pagination.

    Args:
        page (int): Page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        tuple: A tuple containing start and end indices for the requested page.
    """
    start = 0
    end = 0

    for i in range(page):
        start = end
        end += page_size

    return (start, end)
