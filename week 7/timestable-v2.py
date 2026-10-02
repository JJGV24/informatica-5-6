
def main():



    ##this is a failure profe, the one called experiment is actually the timestablev2 asingment :)



    bye = True
    print("welcome to hell")
    print("A program capable of making a monkey like you learn the multiplication tables")


    while bye:
        x = input("Enter a times table that you would like to be tested on: ").strip().lower()
        max_value = int(input("Up to what number would you like it to go to? "))

        print(f"You will be tested in the {x} table")
        if x == "exit":
            break

        else:
            night = True
            for i in range(max_value):
                while night:
                    x = int(x)
                    i += 1
                    z = i * x
                    while ans != z:
                        ans = int(input(f"what is {i} times {x}? "))
                        if ans == z:
                            print("correct")
                        else:
                            print("incorrect")




















if __name__=="__main__":
    main()
