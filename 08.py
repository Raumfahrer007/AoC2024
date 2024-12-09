def get_antenna_locations(input):
    antenna_locations = {}
    for i, line in enumerate(input):
        line = line.replace("\n", "")
        for j, antenna in enumerate(line):
            if not antenna == ".":
                if antenna in antenna_locations:
                    antenna_locations[antenna].append([i, j])
                else:
                    antenna_locations[antenna] = [[i, j]]

    return antenna_locations


def get_antinodes_locations(location, next_location, y_border, x_border, recursive=False):
    temp_antinodes = []
    if location[1] < next_location[1]:
        temp_antinodes.append([location[0] - abs(next_location[0] - location[0]), location[1] - abs(next_location[1] - location[1])])
        temp_antinodes.append([next_location[0] + abs(next_location[0] - location[0]), next_location[1] + abs(next_location[1] - location[1])])
    else:
        temp_antinodes.append([location[0] - abs(next_location[0] - location[0]), location[1] + abs(location[1] - next_location[1])])
        temp_antinodes.append([next_location[0] + abs(next_location[0] - location[0]), next_location[1] - abs(location[1] - next_location[1])])

    valid_antinodes = []
    for antinode in temp_antinodes:
        if antinode[0] >= 0 and antinode[0] < y_border:
            if antinode[1] >= 0 and antinode[1] < x_border:  #-1 because of \n
                valid_antinodes.append(antinode)

    if recursive:
        for antinode in valid_antinodes:
            if antinode[0] < location[0]:
                valid_antinodes + get_antinodes_of_antinodes(antinode, location, y_border, x_border, valid_antinodes, direction="up")
            else:
                valid_antinodes + get_antinodes_of_antinodes(next_location, antinode, y_border, x_border, valid_antinodes, direction="down")

    return valid_antinodes
            

def get_antinodes_of_antinodes(location, next_location, y_border, x_border, valid_antinodes, direction):
    next_antinode = [-1, -1]
    if direction == "up":
        if location[1] < next_location[1]:
            next_antinode = [location[0] - abs(next_location[0] - location[0]), location[1] - abs(next_location[1] - location[1])]
        else:
            next_antinode = [location[0] - abs(next_location[0] - location[0]), location[1] + abs(location[1] - next_location[1])]
    else:
        if next_location[1] < location[1]:
            next_antinode = [next_location[0] + abs(next_location[0] - location[0]), next_location[1] - abs(next_location[1] - location[1])]
        else:
            next_antinode = [next_location[0] + abs(next_location[0] - location[0]), next_location[1] + abs(location[1] - next_location[1])]

    if next_antinode[0] >= 0 and next_antinode[0] < y_border:
        if next_antinode[1] >= 0 and next_antinode[1] < x_border:  #-1 because of \n
            if direction == "up":
                valid_antinodes.append(next_antinode)
                get_antinodes_of_antinodes(next_antinode, location, y_border, x_border, valid_antinodes, direction)
            else:
                valid_antinodes.append(next_antinode)
                get_antinodes_of_antinodes(next_location, next_antinode, y_border, x_border, valid_antinodes, direction)
            
    return valid_antinodes


def part_one(input):
    antenna_locations = get_antenna_locations(input)
    antinodes = set()
    for antenna in antenna_locations:
        for i, location in enumerate(antenna_locations[antenna]):
            for next_location in antenna_locations[antenna][i + 1:]:
                valid_anitnodes = get_antinodes_locations(location, next_location, y_border=len(input), x_border=len(input[0]) - 1)

                for antinode in valid_anitnodes:
                    antinodes.add(tuple(antinode))

    print("PartOne: " + str(len(antinodes)))


def part_two(input):
    antenna_locations = get_antenna_locations(input)
    antinodes = set()
    for antenna in antenna_locations:
        for i, location in enumerate(antenna_locations[antenna]):
            antinodes.add(tuple(location))  #every antenna now also is an antidode
            for next_location in antenna_locations[antenna][i + 1:]:
                valid_antinodes = get_antinodes_locations(location, next_location, y_border=len(input), x_border=len(input[0]) - 1, recursive=True)

                for antinode in valid_antinodes:
                    antinodes.add(tuple(antinode))

    print("PartTwo: " + str(len(antinodes)))

                    

example = [
    "............\n",
    "........0...\n",
    ".....0......\n",
    ".......0....\n",
    "....0.......\n",
    "......A.....\n",
    "............\n",
    "............\n",
    "........A...\n",
    ".........A..\n",
    "............\n",
    "............\n"
]

data = open("08.txt", "r")
input = data.readlines()
data.close()

part_one(input)
part_two(input)