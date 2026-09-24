


def main():


    while True:
        x = input("what table would you like to learn now? ").strip().lower()

        if x == "exit":
            break
        else:
            for i in range(10):
                if int(x)<1 or int(x)>10:
                    print("table not available")
                    break
                else:
                    x = int(x)
                    i += 1
                    z = i * x
                    print(f"{i} times {x} is equal to {z}")













if __name__=="__main__":
    main()
