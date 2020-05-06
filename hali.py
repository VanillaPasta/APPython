import math
import sys

Cs = 30.2
Pu = 87.7
H3 = 12.3

def print_halflife(element_name, halflife, time):
    pernuc = 1.0 * math.pow(0.5, (time/halflife))
    percentage = pernuc * 100
    print('{}: {:.1f}%'.format(element_name, percentage))

def main():
    args = sys.argv
    time = args[1]
    time = float(time)
    print_halflife('Cesium-137', Cs, time)
    print_halflife('Plutonium-238', Pu, time)
    print_halflife('Tritium', H3, time)




main()
