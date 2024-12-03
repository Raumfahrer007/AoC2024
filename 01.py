def get_numbers_from_input(input):
    left_side = []
    right_side = []

    for line in input:
        numbers = line.split()
        left_side.append(int(numbers[0]))
        right_side.append(int(numbers[1]))

    return sorted(left_side), sorted(right_side)


def part_one(input):
    left_side, right_side = get_numbers_from_input(input)
    sum = 0

    for i in range(len(input)):
        sum += abs(left_side[i] - right_side[i])

    print("PartOne: " + str(sum))
#----

def part_two(input):
    left_side, right_side = get_numbers_from_input(input)
    sum = 0

    for number in left_side:
        count = right_side.count(number)
        sum += number * count

    print("Part Two: " + str(sum))
#----

data = open("01.txt", "r")
input = data.readlines()
data.close()

example = [
    "3   4\n",
    "4   3\n",
    "2   5\n",
    "1   3\n",
    "3   9\n",
    "3   3\n"
]

part_one(input)
part_two(input)