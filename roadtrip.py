import time

def main():

    answer = ""
    answ = ""

    while answer != "Yes!":
        time.sleep(1.5)
        answer = input("Are we there yet? ").title().strip()
    if answer == "Yes":
        answ = input("Really? ").title().strip()
        if answ == "Yes":
            print("YEAAAAAAAH BUDDY")


    print("We are here!")



if __name__=="__main__":
    main()
