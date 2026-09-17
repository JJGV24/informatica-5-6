
def main():

    to_do = ["Gym","Go to school"]
    answ = ""
    while answ != exit:

        print("What would you like to do today?")

        answ = input("add, remove, daycomplete, exit\n: ").strip().lower()

        if answ == "add":
            print(to_do)
            add = input("What would you like to add to your to do list? ")
            where = int(input("what position? "))
            where -= 1
            to_do.insert(where, add)
            print("Item added to the list")
        elif answ == "remove":
            print(to_do)
            remove = input("What would you like to remove from your to do list? ")
            to_do.remove(remove)
            print("Item Removed")
        elif answ == "daycomplete":
            to_do.clear
            print("You have completed all items")
        elif answ == "exit":
            break

        print(to_do)









if __name__=="__main__":
    main()


