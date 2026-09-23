


def main():

    ans = input("want to learn a table? ").lower()

    while  ans != "exit":
        x = input("what table would you like to learn now? ")

        for i in range(10):
            x = int(x)
            if x<1 or x>10:
                print("table not available")
                break
            elif x == "exit":
                break
            else:
                i += 1
                z = i * x
                print(f"{i} times {x} is equal to {z}")










if __name__=="__main__":
    main()
