from collections import defaultdict

def add_padding(input):
    input_padding = []
    input_padding.append("." * len(input[0]))
    for line in input:
        input_padding.append("." + line.replace("\n", "") + ".")

    input_padding.append("." * len(input_padding[0]))

    return input_padding


def next_plant(plant_coords, input, visited, region):
    operations = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    new_region = region.copy()
    perimeter = 0
    for operation in operations:
        current_plant = input[plant_coords[0]][plant_coords[1]]
        new_i = plant_coords[0] + operation[0]
        new_j = plant_coords[1] + operation[1]

        #if a neighbor of a plant is not part of the region, then ...
        if not input[new_i][new_j] == current_plant:
            perimeter += 1
            #... the i/j coordinate of the plant is added to a dict of the corresponding j/i
            # in different dicts based on where the part outside of the region is located (above, below, left, right)
            if operation == [-1, 0]:
                new_region["borders"]["ha"][plant_coords[0]].append(plant_coords[1])
            elif operation == [1, 0]:
                new_region["borders"]["hb"][plant_coords[0]].append(plant_coords[1])
            elif operation == [0, -1]:
                new_region["borders"]["vl"][plant_coords[1]].append(plant_coords[0])
            else:
                new_region["borders"]["vr"][plant_coords[1]].append(plant_coords[0])
        else:
            if not tuple([new_i, new_j]) in visited:
                visited.add(tuple([new_i, new_j]))
                new_region = next_plant([new_i, new_j], input, visited, new_region)
            else:
                continue

    new_region["perimeter"].append(perimeter)
    return new_region


def get_regions(input):
    regions = defaultdict(list)
    visited = set()
    
    i = 1
    while i < len(input) - 1:
        j = 1
        while j < len(input[i]) - 1:
            plant = input[i][j]
            if not tuple([i, j]) in visited:
                visited.add(tuple([i, j]))
                region = {
                    "perimeter": [],
                    "borders": {
                        "ha": defaultdict(list),   #horizontal-above
                        "hb": defaultdict(list),   #horizontal-below
                        "vl": defaultdict(list),   #vertical-left
                        "vr": defaultdict(list)    #vertical-right
                    }
                }
                region = next_plant([i, j], input, visited, region)
                regions[plant].append(region)
            j += 1
        i += 1

    return regions


def part_one(input):
    input_padding = add_padding(input)
    regions = get_regions(input_padding)
    
    cost = 0
    for _, plant_type_regions in regions.items():
        for region in plant_type_regions:
            perimeter_list = region["perimeter"]
            cost += len(perimeter_list) * sum(perimeter_list)

    print("PartOne: " + str(cost))


def part_two(input):
    input_padding = add_padding(input)
    regions = get_regions(input_padding)

    cost = 0
    for _, plant_type_regions in regions.items():
        for region in plant_type_regions:
            #every region has four dicts for every possible side of the fence based on a plants position (above, below, left, right)
            #each of these dicts has again dicts based on the i (horizontal) and j (vertical) coordinates of the plants
            #these dicts contain each a sorted list with the corresponding j (horizontal) and i (vertical) coordinates
            #the lists are iterated in order. If the order is interrupted (a coordinate is missing), the fence-side stops, so it increments the count
            border_count = 0
            for _, border_dict in region["borders"].items():
                for _, border_list in border_dict.items():
                    for border in sorted(border_list):
                        if not border + 1 in border_list:
                            border_count += 1

            number_of_plants = len(region["perimeter"])
            cost += number_of_plants * border_count
    
    print("PartTwo: " + str(cost))
            

example = [ #1260
    "RRRRIICCFF\n",
    "RRRRIICCCF\n",
    "VVRRRCCFFF\n",
    "VVRCCCJFFF\n",
    "VVVVCJJCFE\n",
    "VVIVCCJJEE\n",
    "VVIIICJJEE\n",
    "MIIIIIJJEE\n",
    "MIIISIJEEE\n",
    "MMMISSJEEE\n"
]

data = open("12.txt", "r")
input = data.readlines()
data.close()

part_one(input)
part_two(input)