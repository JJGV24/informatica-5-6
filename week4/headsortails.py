import random

def main():

    guess = int(input("Heads(1) or Tails(2): "))

    abc = random.randint(1,2)


    if abc == 1:
        print("Heads")
    elif abc == 2:
        print("Tails")

    if guess == abc:
        print("YOU WIN")
    else:
        print("you lose :(")

if __name__=="__main__":
    main()

