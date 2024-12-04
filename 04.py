import re

def prepare_input(input):   #Returns input as one string and length of one line
    line_length = len(input[0])
    input_string = ""
    for line in input:
        input_string += line.replace("\n", "-")

    return input_string, line_length


#Function to find all matches, beacuse re.findall() does not find overlapping matches
def find_all_matches(regex_pattern, input_string):
    compiled_pattern = re.compile(regex_pattern)
    pos = 0
    findings = []
    while m := compiled_pattern.search(input_string, pos):
        pos = m.start() + 1
        findings.append(m[0])
    return findings


def find_xmas(input_string, line_length):
    gab_between = line_length - 1
    xmas_expression_forw = r"(X.{%s}M.{%s}A.{%s}S)"
    xmas_expression_back = r"(S.{%s}A.{%s}M.{%s}X)"
    regex_patterns_all_directions = []   #Horizontal, Vertical, Diagonal /, Diagonal \
    gab_between_manipulation = [
        0,                  #Horizontal
        gab_between,        #Vertical
        gab_between - 1,    #Diagonal /
        gab_between + 1     #Diagonal \
    ]

    for manipulation in gab_between_manipulation:
        regex_patterns_all_directions.append(xmas_expression_forw %(manipulation, manipulation, manipulation))
        regex_patterns_all_directions.append(xmas_expression_back %(manipulation, manipulation, manipulation))

    all_xmas_occurances =0
    for regex_pattern in regex_patterns_all_directions:
        occurances = len(find_all_matches(regex_pattern, input_string))
        all_xmas_occurances += occurances

    return all_xmas_occurances

def part_one(input):
    input_string, line_length = prepare_input(input)
    all_xmas_occurances = find_xmas(input_string, line_length)

    print("PartOne: " + str(all_xmas_occurances))


def part_two(input):
    x = len(input[0]) - 1 #Without \n
    y = len(input)

    mas_helper_dict = {
        "M": "S",
        "S": "M",
        "X": "",
        "A": ""
    }

    mas_count = 0
    for i in range(1, y-1):   #vertical direction from second row to last but one
        for j in range(1, x-1): #horizontal direction from second place to last but one

            #Look for every "A" if it builds a "MAS" cross
            if input[i][j] == "A":
                up_left = input[i-1][j-1]
                up_right = input[i-1][j+1]

                bottom_left = input[i+1][j-1]
                bottom_right = input[i+1][j+1]

                if mas_helper_dict[up_left] == bottom_right and mas_helper_dict[up_right] == bottom_left:
                    mas_count += 1
                
            j += 1
        i += 1

    print("PartTwo: " + str(mas_count))


example = [
    "MMMSXXMASM\n",
    "MSAMXMSMSA\n",
    "AMXSXMAAMM\n",
    "MSAMASMSMX\n",
    "XMASAMXAMM\n",
    "XXAMMXXAMA\n",
    "SMSMSASXSS\n",
    "SAXAMASAAA\n",
    "MAMMMXMMMM\n",
    "MXMXAXMASX\n"
]

data = open("04.txt", "r")
input = data.readlines()
data.close()

part_one(input)
part_two(input)