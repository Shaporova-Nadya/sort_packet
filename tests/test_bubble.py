import pytest
from bubble import bubble

def test_bubble():
    assert bubble([2, 99, 4, 1]) == [1, 2, 4, 99]


def test_bubble_empty():
    assert bubble([]) == []


def test_bubble_sorted():
    assert bubble([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_bubble_big_num():
    assert bubble([665, 434, 999, 778]) == [434, 665, 778, 999]