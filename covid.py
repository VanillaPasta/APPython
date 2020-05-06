import sys
import math

def main():
    args = sys.argv
    start = args[1]
    pct = args [2]
    start = int(start)
    pct = float(pct)
    pct = 1+(pct/100)
    cur = start
    for x in range(0,14,1):
        print(x,cur)
        cur = cur * pct
        cur = math.floor(cur)

main()
