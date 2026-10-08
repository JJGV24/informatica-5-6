

def main():

    def binary_to_decimal(a):
        print(a)
        
        x = 1

        for i in a:
            x = x * 2
            x += i
        print(x)








    print("Binary to Decimal Converter")
    print("This program will convert any binary number to decimal form")
    binary = input("Enter a binary number: ")
    list(binary)

    binary_to_decimal(binary)




if __name__ == "__main__":
    main()

