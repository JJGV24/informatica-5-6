#define main()
#       print(welcome to hangyourself hangman game)
#       assing random words using random to a variable list
#   define hangyourself function
#       print how many letters there is in the word using len
#       in  while loop
#       ask the user for letter and asign it to a variable
#       create a varieble for tries (5)
#       check if the user input is in the list
#       print correct and where the letter is located or wrong
#       if the answer is wrong take a trie away and print the tries remaining
#       if they get it correct before the tries run out break the loop print congrats
#       if they dont get it print you are sorry then print the correct answer
#
#

import random
def main():


    hangyourself()


def hangyourself():
    with open("ranwords.txt") as new_file:
        content = new_file.read().splitlines()
        word = random.choice(content)
        line = ["_"]* len(word)
        print(" ".join(line))

    while True:
        guess = input("take a guess: ")
        if len(guess) == 1:
            break
        else:
            print("invalid guess")




if __name__ == "__main__":
    main()
