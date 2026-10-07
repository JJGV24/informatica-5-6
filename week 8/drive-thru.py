def main():

    def welcome():
        print("Welcome to twin mountains!")
        menu = ["Cheeseburger", "Fries", "Soda", "Ice Cream", "Cookie"]
        x = 0
        y = 1
        print("Here is the menu:")
        for i in menu:
            print(f"{y}. {menu[x]}")
            x += 1
            y += 1


    def get_item(a):
        a -= 1
        menu = ["🍔", "🍟", "🥤", "🍦", "🍪"]
        print("Here you goo")
        print(menu[a])



    welcome()
    z = int(input("Enter the number of item you would like: "))
    get_item(z)




if __name__ == "__main__":
    main()
