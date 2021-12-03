def find_inc(filename):
    counter = 1
    a_list = []

    with open(filename) as file:
        for line in file:
            line.strip()
            a_list.append(int(line))
        for i in range(len(a_list)):
            if i == 0:
                continue
            if a_list[i-1] < a_list[i]:
                counter += 1
        return counter


def main():

    print(find_inc("data/day01_1.txt"))

if __name__ == "__main__":
    main()