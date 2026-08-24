import time

def main():

    x = 9
    password = "password"
    ppword = input("enter the password: ")


    if ppword == password:
        print("you have succesfully entered Epstein island")

    else:
       print("Incorrect, thanks for trying -Mr. Epstein")


    print("this program will self destruct in 10 seconds.")
    for i in range(9):
        time.sleep(1)
        print(x)
        x = x - 1
    time.sleep(2)
    print("SYSTEM DELETED")



if __name__ == "__main__":
    main()

