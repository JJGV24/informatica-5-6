import random

def main():

    coin = ["heads","tails"]
    attempts = 3

    while attempts > 0:
        guess = input("Heads or Tails?: ").strip().lower()
        flip = random.choice(coin)


        if flip == "heads":
            print("Heads")
        elif flip == "tails":
            print("Tails")

        if flip == guess:
            print("YOU WIN")
            break
        else:
            print("you lose :(")
            attempts -= 1
            print("Attempts left:", attempts)

if __name__=="__main__":
    main()

