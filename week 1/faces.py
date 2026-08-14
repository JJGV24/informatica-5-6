
def main():

    masterpiece = input(" ")

    masterpiece = masterpiece.replace(":)","🙂", count=-1)
    masterpiece = masterpiece.replace(":(","🙁", count=-1)
    print(f"{masterpiece}")

if __name__ == "__main__":
    main()
