# OPTION 1 - FIND DUPLICATE
# DO NOT SHARE

from typing import List

# Implement a function to identify a duplicate integer in an unsorted array
# of integers. Talk about time/space complexity for each method you implement.

# `input` contains exactly N+1 numbers
# `input` elements are integers in the domain [1, N]
# `input` contains all integers in the domain [1, N] at least once
# `findDuplicate` returns an `int`: the duplicate integer

# For the first function, I used a set to track encountered integers, and return
# the first duplicate integer. If there is no duplicate, the function returns -1.
def findDuplicate_one(input: List[int]) -> int:
    s: set[int] = set()
    for num in input:
        if num not in s:
	    s.add(num)
        else:
            return num
    return -1

# For the second function, I used the bitwise XOR operator to find the first 
# duplicate integer when the XOR returns 0. If there is no duplicate, the function 
# returns -1. 
def findDuplicate_two(input: List[int]) -> int:
    if len(input) == 0:
	return -1
    x: int = input[0]
    for num in input[1:]:
	if x ^ num == 0:
	    return num
    return -1

# I am not completely sure of the exact time/space complexity, but I believe my 
# first implementation has a higher time and space complexity because of my usage
# of the set. In my second function, I don't use any data structure that takes 
# up storage, so I think the time and space complexity are smaller. 


