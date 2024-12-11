from collections import defaultdict

def format_input_to_dict(input):
    return {item: 1 for item in input.replace("\n", "").split(" ")}


def blink(stone_dict):
    new_dict = defaultdict(int)
    for stone, count in stone_dict.items():
        if stone == "0":
            new_dict["1"] += count

        elif len(stone) % 2 == 0:
            mid_of_stone = len(stone) // 2
            new_dict[stone[:mid_of_stone]] += count
            new_dict[str(int(stone[mid_of_stone:]))] += count

        else:
            new_dict[str(int(stone) * 2024)] += count

    return new_dict


def part_one(input):
    stone_dict = format_input_to_dict(input)
    for _ in range(25):
        stone_dict = blink(stone_dict)

    print(sum(stone_dict.values()))


def part_two(input):
    stone_dict = format_input_to_dict(input)
    for _ in range(75):
        stone_dict = blink(stone_dict)

    print(sum(stone_dict.values()))


example = "125 17"

data = open("11.txt", "r")
input = data.read()
data.close()

part_one(input)
part_two(input)