#! /usr/bin/env python
import sys

def main(args):
    nums = [3, 6.5]
    the_max = get_max(nums)
    print(the_max)
    the_min = get_min(nums)
    print(the_min)
    range = the_max - the_min
    print (range)
    the_avg = get_avg(nums)
    print (the_avg)

def get_avg(nums):
    total=0
    for n in nums:
        total = total + n
    avg = total / len(nums)
    return avg

def get_max(nums):
    mx = nums[0]
    for n in nums:
        if n > mx:
            mx = n
    return mx

def get_min(nums):
    mn = nums[0]
    for n in nums:
        if n < mn:
            mn = n
    return mn

main(sys.argv)
