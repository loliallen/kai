def read_input(prefix = ""):
    """
        reads data from stdin\n
        data: item, price
    """
    number = input("Enter number: ")
    return (number)

def sum_of_digits(number):
    sum = 0
    for i in number:
        sum += int(i)
    return sum

if __name__ == "__main__":
    number = read_input()
    if(number.isdigit()):
        sum = sum_of_digits(number)
        print("Sum of digits : ".format(sum))
    else:
        print("Bee... 🤢. ...🤮")
