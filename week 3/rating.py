def main():

    print("Thanks for dinning at Los Pollos Hermanos Family!")

    rating = float(input("Rate us in a scale from 1 - 5: "))
    if rating > 5:
        rating = 5
    elif rating < 0:
        rating = 0

    if rating >= 4.5:
        print("Absolute Rooster")

    elif rating >= 4:
        print("Excellent Pollo Night")

    elif rating >= 3:
        print("Good Chicken")

    elif rating >= 2:
        print("Fair ChickenLittle")

    else:
        print("Poor ChickenLittle")

    print("Hope to see you again! Have a great night.")

if __name__ == "__main__":
    main()
