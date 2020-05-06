import sys

def main():
    args = sys.argv
    far = args[1]
    far = int(far)
    print(far)
    cel = (far -32) * 5/9
    print(cel)
    kel = (cel + 273)
    print(kel)


main()
