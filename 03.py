import re
def get_sum_from_input(input):
    expression = r"mul\([0-9]{1,3}\,[0-9]{1,3}\)"
    findings = re.findall(expression, input)

    numbers = []
    for finding in findings:
        finding = finding.replace("mul(", "").replace(")", "")
        numbers.append(finding.split(","))

    sum = 0
    for number_pair in numbers:
        sum += (int(number_pair[0]) * int(number_pair[1]))

    return sum



def part_one(input):
    sum = get_sum_from_input(input)
    print("PartOne: " + str(sum))


def part_two(input):
    expression_do = r"do\(\)"
    expression_dont = r"don't\(\)"

    do_indices = [m.start(0) for m in re.finditer(expression_do, input)]    #All indices where do starts
    do_indices.insert(0, 0)
    dont_indices = [m.start(0) for m in re.finditer(expression_dont, input)]    #All indices where dont starts

    do_input_parts = [] #All parts of the input that count

    i = 0
    k = 0
    #Loops find Do and the next Dont, save pair in list and repeat for next Do after previous Dont
    while i < len(do_indices):
        while k < len(dont_indices):
            if dont_indices[k] > do_indices[i]:
                do_input_parts.append([do_indices[i], dont_indices[k]])

                while do_indices[i] < dont_indices[k]:  #find the next Do after the previous Dont
                    i += 1
                    if i == len(do_indices) - 1:
                        i += 1  #Terminate outter while loop
                        break
                break
            else:
                if k == len(dont_indices) - 1:
                    do_input_parts.append([do_indices[i], -1])
                    i = len(do_indices)
                    break
                else:
                    k += 1
        
    sum = 0        
    for part in do_input_parts:
        sum += get_sum_from_input(input[part[0]:part[1]])

    print("PartTwo: " + str(sum))
        

example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
example2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

data = open("03.txt", "r")
input = data.read()
data.close()

part_one(input)
part_two(input)