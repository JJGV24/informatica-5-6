
import random

def main():

    nombre = input("Whats your name? ")
    print(f"hello {nombre}, lets play a game")
    dif = int(input("Choose a dificulty level:[1]Easy, [2]Medium, [3]Hard "))

    if dif == 1:
        numb = random.randit(1,20)
        print("I'm thinking of a number between 1-20")
        guess = int(input("Take a guess: "))
            while guess != numb:
                if guess < numb:
                    print("too low")
                    guess = int(input("Take a guess: "))
                elif guess > numb:
                    print("too high")
                    guess = int(input("Take a guess: "))
    print(f"congrats {nombre}, You guessed the number!")










if __name__=="__main__":
    main()
