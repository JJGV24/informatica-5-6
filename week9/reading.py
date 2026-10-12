
def main():
    #Read a file
    #with open("sample.txt") as new_file:
     #   content = new_file.read()
    #    print(content)

#Turn file into a list
    #count = 0
    #with open("sample.txt") as hoco_week:
     #   for line in hoco_week:
      #      line = line.replace("\n","")
       #     count += 1
        #    print(f"Day {count}: {line}")


    # Assignment
    def largest(file):
        with open(file) as numberfile:
            for number in numberfile:
                number = number.replace("\n","")
                numberlist.append(int(number))

        print(max(numberlist))



    with open("random.txt") as nfile:
        content = nfile.read()
        print(content)
    largest(nfile)

    with open("random.txt") as nffile:
        for line in nffile:
            line = line.replace("\n","")

        largest(nffile)

if __name__ == "__main__":
    main()
