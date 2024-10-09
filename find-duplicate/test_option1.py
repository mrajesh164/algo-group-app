import pytest
from option1 import findDuplicate_one
from option1 import findDuplicate_two

t1 = []
t2 = [1]
t3 = [1, 7, 3, 4, 2, 4, 6, 5]
t4 = [3, 3, 2, 1]

def test_cases():
    assert findDuplicate_one(t1) == -1
    assert findDuplicate_two(t1) == -1
    assert findDuplicate_one(t2) == -1
    assert findDuplicate_two(t2) == -1
    assert findDuplicate_one(t3) == 4
    assert findDuplicate_two(t3) == 4
    assert findDuplicate_one(t4) == 3
    assert findDuplicate_two(t4) == 3
