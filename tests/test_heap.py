import pytest
from heap import heap_sort


def test_heap():
    assert heap_sort([3, 9, 4, 10]) == [3, 4, 9, 10]


def test_heap_empty():
    assert heap_sort([]) == []


def test_heap_sorted():
    assert heap_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_heap_big_num():
    assert heap_sort([665, 434, 999, 778]) == [434, 665, 778, 999]