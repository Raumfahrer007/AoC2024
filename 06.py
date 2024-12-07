def find_start_position_and_direction(input):
    for line_count, line in enumerate(input):
        line = line.replace("\n", "")
        if not "^" in line:
            continue
        else:
            for column_count, object in enumerate(line):
                if object == "^":
                    return [line_count, column_count], "N"
                
def get_visited_positions(input, current_position, current_direction):  #Set of visited positions | Set of intersections | Loop or not
    walked_way = {
        "N": [],
        "E": [],
        "S": [],
        "W": [],
    }
    route_finished = False
    loop = False
    visited_positions = set()

    while not route_finished:
        if current_position in walked_way[current_direction]:
            loop = True
            route_finished = True
            break
        else:
            walked_way[current_direction].append(current_position.copy())
            visited_positions.add(tuple(current_position))

            match current_direction:
                case "N":
                    if current_position[0] > 0:
                        if not input[current_position[0] - 1][current_position[1]] == "#":
                            current_position[0] -= 1
                        else:
                            current_direction = "E"
                    else:
                        route_finished = True
                case "E":
                    if current_position[1] < len(input[current_position[0]]) - 1:
                        if not input[current_position[0]][current_position[1] + 1] == "#":
                            current_position[1] += 1
                        else:
                            current_direction = "S"
                    else:
                        route_finished = True
                case "S":
                    if current_position[0] < len(input) - 1:
                        if not input[current_position[0] + 1][current_position[1]] == "#":
                            current_position[0] += 1
                        else:
                            current_direction = "W"
                    else:
                        route_finished = True
                case "W":
                    if current_position[1] > 0:
                        if not input[current_position[0]][current_position[1] - 1] == "#":
                            current_position[1] -= 1
                        else:
                            current_direction = "N"
                    else:
                        route_finished = True

    return visited_positions, loop


def part_one(input):
    current_position, current_direction = find_start_position_and_direction(input)
    visited_positions, _= get_visited_positions(input, current_position, current_direction)

    print("PartOne: " + str(len(visited_positions)))


def part_two(input):
    current_position, current_direction = find_start_position_and_direction(input)
    start_position = tuple(current_position)
    visited_positions, _ = get_visited_positions(input, current_position.copy(), current_direction)
    visited_positions.remove(start_position)

    loop_count = 0
    for i, potential_obstacle_postion in enumerate(visited_positions):
        if i % 100 == 0: print(i)
        new_input = input.copy()
        new_input[potential_obstacle_postion[0]] = new_input[potential_obstacle_postion[0]][:potential_obstacle_postion[1]] + "#" + new_input[potential_obstacle_postion[0]][potential_obstacle_postion[1] + 1:]

        _, loop = get_visited_positions(new_input, current_position.copy(), current_direction)
        if loop:
            loop_count += 1

    print("PartTwo: " + str(loop_count))


example = [
    "....#.....\n",
    ".........#\n",
    "..........\n",
    "..#.......\n",
    ".......#..\n",
    "..........\n",
    ".#..^.....\n",
    "........#.\n",
    "#.........\n",
    "......#...\n"
]

data = open("06.txt", "r")
input = data.readlines()
data.close()

part_one(input)
part_two(input)