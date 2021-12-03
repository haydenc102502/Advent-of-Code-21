def position(filename):
    with open(filename) as file:
        x = 0
        y = 0
        aim = 0
        for line in file:
            if line[0] == "f":
                x += int(line[len(line) - 2])
            elif line[0] == "d":
                y += int(line[len(line) - 2])
            else:
                y -= int(line[len(line) - 2])
        return x * y

def position_with_depth(filename):
    with open(filename) as file:
        x = 0
        y = 0
        aim = 0
        for line in file:
            if line[0] == "d":
                aim += int(line[len(line) - 2])
            elif line[0] == "u":
                aim -= int(line[len(line) - 2])
            else:
                x += int(line[len(line) - 2])
                y += aim * int(line[len(line) - 2])
        return x * y



def main():

    print(position_with_depth("data/day02.txt"))

if __name__ == "__main__":
    main()