
import random

def main():

    nombre = input("Whats your name? ")
    print(f"hello {nombre}, lets play a game")
    dif = int(input("Choose a dificulty level:[1]Easy, [2]Medium, [3]Hard "))

    if dif == 1:
        numb = random.randint(1,20)
        print("I'm thinking of a number between 1-20")
        guess = int(input("Take a guess: "))
        att = 5
        while att > 0:
            if guess < numb:
                print("too low")
                att -= 1
                print(f"Remaining attempts:{att}")
                guess = int(input("Take a guess: "))
            elif guess > numb:
                print("too high")
                att -= 1
                guess = int(input("Take a guess: "))
            elif guess == numb:
                print(f"congrats {nombre}, You guessed the number!")
                break

    elif dif == 2:
        numb = random.randint(1,50)
        print("I'm thinking of a number between 1-50")
        guess = int(input("Take a guess: "))
        att = 7
        while att > 0:
            if guess < numb:
                print("too low")
                att -= 1
                print(f"Remaining attempts:{att}")
                guess = int(input("Take a guess: "))
            elif guess > numb:
                print("too high")
                att -= 1
                guess = int(input("Take a guess: "))
            elif guess == numb:
                print(f"congrats {nombre}, You guessed the number!")
                break

    elif dif == 3:
        numb = random.randint(1,100)
        print("I'm thinking of a number between 1-100")
        guess = int(input("Take a guess: "))
        att = 10
        while att > 0:
            if guess < numb:
                print("too low")
                att -= 1
                print(f"Remaining attempts:{att}")
                guess = int(input("Take a guess: "))
            elif guess > numb:
                print("too high")
                att -= 1
                guess = int(input("Take a guess: "))
            elif guess == numb:
                print(f"congrats {nombre}, You guessed the number!")
                break










if __name__=="__main__":
    main()
