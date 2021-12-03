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

def find_inc_sums(filename):
    counter = 1
    a_list = []
    sums = []
    sum = 0

    with open(filename) as file:
        for line in file:
            line.strip()
            a_list.append(int(line))
        for i in range(len(a_list) - 2):
            sum = a_list[i] + a_list[i + 1] + a_list[i + 2]
            sums.append(sum)
        for i in range(len(sums)):
            if i == 0:
                continue
            if sums[i-1] < sums[i]:
                counter += 1
        return counter



def main():

    print(find_inc_sums("data/day01.txt"))

if __name__ == "__main__":
    main()