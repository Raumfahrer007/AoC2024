def input_as_list(input):
    list = []
    for i, value in enumerate(input):
        if i % 2 == 0:  #File
            list = list + ([i//2] * int(value))
        else:
            list = list + (["."] * int(value))
    return list


def input_as_blocks(input):
    list = []
    for i, value in enumerate(input):
        if i % 2 == 0:
            list.append([i//2, int(value)])
        else:
            if value == "0":
                continue
            list.append([-1, int(value)])
    list.append([-1, 1])    #buffer
    return list


def part_one(input):
    list = input_as_list(input)
    current_end = len(list) - 1
    for i, value in enumerate(list):
        if value == ".":
            while list[current_end] == ".":
                current_end -= 1
            list[i] = list[current_end]
            del list[current_end]
            current_end -= 1
        
        if i >= current_end:
            break
    
    sum = 0
    for i, value in enumerate(list):
        if value == ".":
            break
        sum += (i * int(value))

    print("PartOne: " + str(sum))


def part_two(input):
    fragment_list = input_as_blocks(input)
    
    index = len(fragment_list) - 2  #skip buffer
    while index > 0:
        fragment = fragment_list[index]

        if fragment[0] == -1:
            index -= 1
        else:
            for j, other_fragment in enumerate(fragment_list[:index]):
                if other_fragment[0] == -1 and other_fragment[1] >= fragment[1]:
                    fragment_list[j] = fragment.copy()
                    fragment_list[index][0] = -1

                    if other_fragment[1] > fragment[1]: #more free space than file size
                        if fragment_list[j + 1][0] == -1:   #add free space to existing free space
                            fragment_list[j + 1][1] += other_fragment[1] - fragment[1]
                        else:   #add new free space
                            fragment_list.insert(j + 1, [-1, other_fragment[1] - fragment[1]])
                            index += 1

                    if fragment_list[index + 1][0] == -1:
                        fragment_list[index][1] += fragment_list[index + 1][1]
                        del fragment_list[index + 1]
                    if fragment_list[index - 1][0] == -1:
                        fragment_list[index - 1][1] += fragment_list[index][1]
                        del fragment_list[index]

                    break
                        
            index -= 1

    sum = 0
    multiplier = 0
    for fragment in fragment_list:
        if fragment[0] == -1:
            multiplier += fragment[1]
        else:
            for _ in range(fragment[1]):
                sum += fragment[0] * multiplier
                multiplier += 1

    print("PartTwo: " + str(sum))

example = "2333133121414131402"

data = open("09.txt", "r")
input = data.read()
data.close()

part_one(input)
part_two(input)