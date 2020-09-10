def read_input(prefix = ""):
    """
        reads data from stdin\n
        data: item, price
    """
    weight, price = list(map(int, input("{}: Input weight, price: ".format(prefix)).split(" ")))
    return (weight, price)


if __name__ == "__main__":
    weightX, priceA = read_input("X")
    weightY, priceB = read_input("Y")

    oneX = priceA / weightX
    oneY = priceB / weightY

    timesXmoreThanY = oneX / oneY

    print("One kg of X: {}\nOne kg of Y: {}\nX more than Y {} times".format(oneX, oneY, timesXmoreThanY))
