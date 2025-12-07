import pytest
from src.sortings.merge import merge_sort


def test_merge():
    assert merge_sort([2, 99, 4, 1]) == [1, 2, 4, 99]


def test_merge_empty():
    assert merge_sort([]) == []


def test_merge_sorted():
    assert merge_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_merge_big_num():
    assert merge_sort([665, 434, 999, 778]) == [434, 665, 778, 999]