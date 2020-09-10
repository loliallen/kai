def find_hypotenyse(a, b):
    """
        method finds a hypothenuse by legs a and b\n
        returns 0 if a or b is not a number
    """
    if(type(a) is int) and (type(b) is int):
        return (a**2 + b**2)**0.5
    return (0)

def read_input():
    """
        reads a, b parameters from stdin
    """
    a = int(input("a: "))
    b = int(input("b: "))
    return a, b

if __name__ == "__main__":
    a, b = read_input()
    print(find_hypotenyse(a, b))
