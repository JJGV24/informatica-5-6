
from datetime import datetime

def main():

    print("What day is it today?")
    day = datetime.now().weekday()
    days = ("monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    print(days{day})
    if day <= 4:
        print("It's a weekday")
        remaining = 5 - day
        print(remaining, "days until the weekend")
    elif day == 4:
        print("It's Friday")
        print("Just a day left until the weekend")
    else:
        print("It's the weekend")

    months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    print("What month is it?)
    month = int(input())
    print("It is", months[month])

    Print("This are the summer months:")
    print(months{5})
    print(months{6})
    print(months{7})

    seasons = ["Winter", "Spring", "Summer", "Autumn"]
    print("What months is it? (1-12)")
    month = int(input())

    if month <= 2 or month == 12:
        season = 0
    elif month <= 5:
        season = 1
    elif month <= 8:
        season = 2
    else:
        season = 3
    print("It is", seasons[season])

    



if __name__=="__main__":
    main()


