import math

def get_results_and_numbers(input):
    results_and_numbers = []
    for line in input:
        line = line.replace("\n", "")
        result = line.split(": ")[0]
        numbers = line.split(": ")[1].split(" ")
        results_and_numbers.append([result, numbers])

    return results_and_numbers

def baseb_str(n, b):
    e = n//b
    q = n%b
    if n == 0:
        return '0'
    elif e == 0:
        return str(q)
    else:
        return baseb_str(e, b) + str(q)
    

"""
code tries every possible combination of +/* or +/*/|| with the given numbers
by generating strings of 0 and 1 (and 2) with the length of the necessary number of operations.
For doing this, it uses binary/ternary numbers and fills rest of length with 0
"""
def equation_is_possible(result, numbers, base):
    operation_count = len(numbers) - 1  #number of necessary operations per try
    max_binary_number = base ** operation_count    #max binary number I can represent with number of necessary operations

    i = 0
    for i in range(max_binary_number):  #number of possible orders
        binary_str = baseb_str(i, base)
        frequency = "0" * (operation_count - len(binary_str)) + binary_str
        number_copy = numbers.copy()

        temp_result = int(number_copy[0])
        for i in range(len(frequency)):
            if frequency[i] == "0":
                temp_result += int(number_copy[i+1])
            elif frequency[i] == "1":
                temp_result *= int(number_copy[i+1])
            else:
                temp_result = int(str(temp_result) + number_copy[i+1])
            
        if temp_result == result:
            return True
    return False


def part_one(input):
    result_and_numbers = get_results_and_numbers(input)
    sum = 0
    
    for equation in result_and_numbers:
        result = int(equation[0])
        numbers = equation[1]
        if equation_is_possible(result, numbers, 2):
            sum += result

    print("PartOne: " + str(sum))


def part_two(input):
    result_and_numbers = get_results_and_numbers(input)
    sum = 0
    #filter all that were possible with + and *
    not_possible = []
    for i, equation in enumerate(result_and_numbers):
        result = int(equation[0])
        numbers = equation[1]
        if equation_is_possible(result, numbers, 2):
            sum += result
        else:
            not_possible.append(equation)
    
    for i, equation in enumerate(not_possible):
        if i % 100 == 0:
            print(i)
        result = int(equation[0])
        numbers = equation[1]
        if equation_is_possible(result, numbers, 3):
            sum += result

    print("PartTwo: " + str(sum))


example = [
    "190: 10 19\n",
    "3267: 81 40 27\n",
    "83: 17 5\n",
    "156: 15 6\n",
    "7290: 6 8 6 15\n",
    "161011: 16 10 13\n",
    "192: 17 8 14\n",
    "21037: 9 7 18 13\n",
    "292: 11 6 16 20\n"
]

data = open("07.txt", "r")
input = data.readlines()
data.close()

#part_one(input)
part_two(input)