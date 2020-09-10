import math


def read_input():
    """
        reads data from stdin\n
        data: r1, r2
    """
    r1, r2 = int(input()), int(input())
    return (r1, r2)

def calculate_area(r):
    """
        method calculates the area of circle, with radius r
    """
    return (math.pi * r**2)

if __name__ == "__main__":
    r1, r2 = read_input()
    s1, s2 = calculate_area(r1), calculate_area(r2)
    s3 = s1 - s2
    print("s1: {}, s2: {}, s3: {}".format(s1, s2, s3))
