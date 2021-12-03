def position(filename):
    with open(filename) as file:
        x = 0
        y = 0
        """
        forward 5
        """
        x = 0
        y = 0
        for line in file:
            if line[0] == "f":
                x += int(line[len(line) - 2])
            elif line[0] == "d":
                y += int(line[len(line) - 2])
            else:
                y -= int(line[len(line) - 2])
        return x * y



def main():

    print(position("data/day02.txt"))

if __name__ == "__main__":
    main()