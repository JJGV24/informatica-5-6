
def main():

    fah = input("Descent atmosphere layer: ")
    sev = str(fah).strip
    sphere = str(sev).lower


    if sphere == "troposphere":
        print("your descent range will be between 0-12km.")
        x = int(input("enter your exact distance of descent in km: "))
        x *= 1000  #km to meters
        x /= 20   #meters divided by velocity = time in seconds?
        x = round(x,1)
        print(f"{x}")

    elif sphere == "stratosphere":
        print("your descent range will be between 12-50km.")
        a = int(input("enter your exact distance of descent in km: "))
        if a == 12:
            print("600")
        else:
            x = a - 12
            x *= 1000
            x /= 75
            x += 600
            x = round(x,1)
            print(f"{x}")

    elif sphere == "mesosphere":
        print("your descent range will be between 50-85km.")
        x = int(input("enter your exact distance of descent in km: "))
        if a == 50:
            print("1106.7")
        else:
            x = a - 50
            x *= 1000
            x /= 200
            x += 1106.7
            x = round(x,1)
            print(f"{x}")

    elif sphere == "thermosphere":
        print("your descent range will be between 85-700km.")
        x = int(input("enter your exact distance of descent in km: "))
        if a == 12:
            print("1281.7")
        else:
            x = a - 85
            x *= 1000
            x /= 500
            x += 1281.7
            x = round(x,1)
            print(f"{x}")

    elif sphere == "exosphere":
        print("your descent range will be between 700-10,000km.")
        x = int(input("enter your exact distance of descent in km: "))
        if a == 12:
            print("600")
        else:
            x = a - 700
            x *= 1000
            x /= 2000
            x += 2511.7
            x = round(x,1)
            print(f"{x}")

    else:
        print("6-7")

if __name__ == "__main__":
    main()
