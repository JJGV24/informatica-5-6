
def main():

    transistores = 17800000000

    years = int(input("How many years into the future: "))

    transistores *= 2**(years/2)


    print(transistores)


if __name__ == "__main__":
    main()
