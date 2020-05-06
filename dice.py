#! /usr/bin/env python

import random
import sys

def roll_dice(num_sides):
    dice_num = random.randint(1,num_sides)
    return dice_num

def main():
    args = sys.argv
    print(sys.argv)
    if len(args) != 2:
        print("pass number of rolls")
        return
    num_rolls = int(args[1])
    results = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    #print(results)
    for x in range(0,num_rolls,1):
        d1 = roll_dice (6)
        d2 = roll_dice (6)
        results[d1 + d2] += 1
    print(results)





main()
