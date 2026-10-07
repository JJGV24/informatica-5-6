def main():
    day1 = [26,26,26,25,24,22,21,21,20]
    day2 = [19,19,18,17,17,16,16,16,18,20,22,24,25,26,27,27,27,27,26,25,23,21,21,20]
    day3 = [19,18,18,17,16,16,16,16,17,20,22,23,25,26,26,26]



    print("Today")
    max_temperature(day1)
    min_temperature(day1)
    print()

    print("Tomorrow")
    max_temperature(day2)
    min_temperature(day2)
    print()
    
    print("Day After Tomorrow")
    max_temperature(day3)
    min_temperature(day3)

def max_temperature(temperatures):
    highest_t = temperatures[0]
    for hour in temperatures:
        if hour > highest_t:
            highest_t = hour
    print(f"High {highest_t}°")

def min_temperature(temperatures):
    lowest_t = temperatures[0]
    for hour in temperatures:
        if hour < lowest_t:
            lowest_t = hour
    print(f"Low {lowest_t}°")



if __name__ == "__main__":
    main()
