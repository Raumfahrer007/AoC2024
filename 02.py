def get_numbers_from_input(input):
    reports = []
    for line in input:
        splitted_line = line.split()
        reports.append([int(number) for number in splitted_line])

    return reports


def find_error(report, increase): #Returns index of error or -1 if none occured
    index = -1
    for i in range(len(report) - 1):
        if report[i] == report[i+1]:
            index = i
            break
        
        elif not (report[i] < report[i+1]) == increase:
            index = i
            break

        elif abs(report[i] - report[i + 1]) > 3:
            index = i
            break
    
    return index


def part_one(input):
    reports = get_numbers_from_input(input)
    sum = 0

    for report in reports:
        safe = True
        if report[0] == report[1]:
            continue
        else:
            increase = True if report[0] < report[1] else False

        for i in range(len(report) -1):
            if not (report[i] < report[i+1]) == increase or report[i] == report[i+1] or abs(report[i] - report[i + 1]) > 3: 
                safe = False
                break

        if safe: sum += 1

    print("Part One: " + str(sum))


def part_two(input):
    reports = get_numbers_from_input(input)
    sum = 0

    for report in reports:
        errors = 0
        increase = None
        safe = True

        #Calculate if report levels increase or decrease
        increase_count = 0
        for k in range(3):
            if errors > 1:
                safe = False
                break

            if report[k]== report[k+1]:
                errors += 1
            else:
                if report[k] < report[k+1]:
                    increase_count += 1
        if safe:
            increase = True if increase_count >= 2 else False
        else:
            continue    #Report unsafe

        #Look for error in report
        index = find_error(report, increase)
        if index > -1:
            safe = False

        #Removes each element once and checks if error still persists
        #If one removal removes error, the report is safe
        i = 0
        while i < len(report) and index > -1:
            report_copy = report.copy()
            del report_copy[i]
            index = find_error(report_copy, increase)
            if index == -1:
                safe = True
                break
            i += 1

        if safe:
            sum += 1

    print("Part Two: " + str(sum))



example = [
    "7 6 4 2 1\n",
    "1 2 7 8 9\n",
    "9 7 6 2 1\n",
    "1 3 2 4 5\n",
    "8 6 4 4 1\n",
    "1 3 6 7 9\n",
]

data = open("02.txt", "r")
input = data.readlines()
data.close()

part_one(input)
part_two(input)