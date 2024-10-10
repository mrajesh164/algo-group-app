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

"""
test results:
Mayas-MacBook-Pro:find-duplicate maya$ pytest
====================================================================== test session starts =======================================================================
platform darwin -- Python 3.12.6, pytest-8.1.1, pluggy-1.4.0
rootdir: /Users/maya/Documents/algo-group-take-home/find-duplicate
plugins: json-report-1.5.0, metadata-3.1.1, mypy-0.10.3, timeout-2.3.1
collected 1 item                                                                                                                                                 

test_option1.py .                                                                                                                                          [100%]

======================================================================= 1 passed in 0.01s ========================================================================
"""
