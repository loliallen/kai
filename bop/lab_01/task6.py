def read_input(prefix = ""):
    """
        reads data from stdin\n
        data: item, price
    """
    number = input("Enter number: ")
    return (number)

def reverse(number):
    return number[::-1]

if __name__ == "__main__":
    number = read_input()
    if(number.isdigit()):
        sum = reverse(number)
        print("Reversed number : {}".format(sum))
    else:
        print("Bee... 🤢. ...🤮")
