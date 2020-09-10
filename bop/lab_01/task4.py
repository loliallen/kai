def read_input(prefix = ""):
    """
        reads data from stdin\n
        data: item, price
    """
    A, B = list(map(int, input("Enter A and B: ".format(prefix)).split(" ")))
    return (A, B)

def get_count_of_sections(a, b):
    """
    method counts an int number of sections
    """
    return ((a - b) // b)

if __name__ == "__main__":
    A, B = read_input()
    if(A > B):
        print("Count of sections: {}".format(get_count_of_sections(A, B)))
    else:        
        print("Bee... 🤢. ...🤮")
