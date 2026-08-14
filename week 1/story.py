def main():
    # planet = input("planet: ")

    # #Separation
    # print("Hello", planet)

    # # Concatenation
    # print("hello " + planet)

    # #Formatted Strings
    # print(f"Hello {planet}")

    # #Ending
    # print("hello", end=" ")
    # print(planet)

    name = input("What is your name? ").strip().title()
    color = input("Pick a color brodie: ").strip().lower()
    adj = input("Gimme an adjective: ").strip().lower()
    Goal = input("What is your life´s goal? \n").strip().lower()

    print(f"Hello, {name}\n\n")

    print("This is your story:")
    print(f"At dawn the sky turned {color}, and the\n air felt {adj}. I decided today I will finally\n {Goal}.")

    yelling = f"At dawn the sky turned {color}, and the\n air felt {adj}. I decided today I will finally {Goal}.\n"
    print(yelling.upper())


if __name__=="__main__":
    main()
