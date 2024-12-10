from operator import add

def add_padding_to_map(input):
    map_input = []
    for line in input:
        line = line.replace("\n", "")
        line = "." + line
        line += "."
        map_input.append(line)
        
    map_input.append("." * len(map_input[0]))
    map_input.insert(0, "." * len(map_input[0]))

    return map_input


def find_all_start(input):
    start_coordinates = []

    for i, line in enumerate(input):
        for j, height in enumerate(line):
            if height == "0":
                start_coordinates.append([i, j])

    return start_coordinates


def check_next_steps(map_input, current_coordinates, trails):
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]] #up, down, left, right
    current_field = int(map_input[current_coordinates[0]][current_coordinates[1]])

    for direction in directions:
        next_coordinates = list(map(add, current_coordinates, direction))
        next_field = map_input[next_coordinates[0]][next_coordinates[1]]

        if next_field == ".":
            continue
        elif  int(next_field) <= current_field or int(next_field) > current_field + 1:
            continue
        elif next_field == "9":
            if isinstance(trails, list):
                trails.append(next_coordinates)
            else:
                trails.add(tuple(next_coordinates))
        else:
            check_next_steps(map_input, next_coordinates, trails)

    return trails


def part_one(input):
    map_input = add_padding_to_map(input)
    start_coordinates = find_all_start(map_input)

    sum = 0
    for start in start_coordinates:
        trails = check_next_steps(map_input, start, set())
        sum += len(trails)

    print("PartOne: " + str(sum))


def part_two(input):
    map_input = add_padding_to_map(input)
    start_coordinates = find_all_start(map_input)

    sum = 0
    for start in start_coordinates:
        trails = check_next_steps(map_input, start, list())
        sum += len(trails)

    print("PartOne: " + str(sum))


example = [
    "89010123\n",
    "78121874\n",
    "87430965\n",
    "96549874\n",
    "45678903\n",
    "32019012\n",
    "01329801\n",
    "10456732\n"
]

data = open("10.txt", "r")
input = data.readlines()
data.close()

part_one(input)
part_two(input)