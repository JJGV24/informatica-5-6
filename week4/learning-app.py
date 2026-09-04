import time
import random
def main():         #⭐


    print("Welcome to Kumen.learn")
    print("Kumen is here to help you learn math.")
    print("Select your opperation type")
    problem = input("(+),(-),(*): ")
    streak = 0


    if problem == "+":
        while streak < 3:
            num1 = random.randint(10,90)
            num2 = random.randint(10,90)

            print("Solve:")
            correct = num1 + num2
            answ = int(input(f"{num1} + {num2}: "))
            if answ != correct:
                print("bruh")
                streak = 0
                time.sleep(5)
                print(f"correct answer was:{correct}")
                print(f"Streak:{streak}")
            elif answ == correct:
                print("Good job bretheren")
                streak += 1
                print(f"streak:{streak}")


if __name__=="__main__":
    main()

