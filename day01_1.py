def find_inc(filename):
    counter = 0
    with open(filename) as file:
        for lines in range(len(file) - 1):
            if file[lines] < file[lines + 1]:
                counter += 1
    return counter


def main():

    print(find_inc("day01_1.txt"))

if __name__ == "__main__":
    main()