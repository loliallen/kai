def read_input(prefix = ""):
    """
        reads data from stdin\n
        data: item, price
    """
    number = input("Enter number: ")
    return (number)

def make_new(number):
    return (number[1:3:1] + number[0] )

if __name__ == "__main__":
    number = read_input()
    if(number.isdigit() and len(number) == 3):
        num = make_new(number)
        print("New number : {}".format(num))
    else:
        print("Bee... 🤢. ...🤮")
