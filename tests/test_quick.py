import pytest
from src.sortings.quick import quick_sort


def test_quick():
    assert quick_sort([2, 99, 4, 1]) == [1, 2, 4, 99]


def test_quick_empty():
    assert quick_sort([]) == []


def test_quick_sorted():
    assert quick_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_quick_big_num():
    assert quick_sort([665, 434, 999, 778]) == [434, 665, 778, 999]