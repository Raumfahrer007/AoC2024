def get_rules_and_updates(input):
    break_point = 0
    rules = {}  #shows all pages that need to be placed before key-page

    for i, line in enumerate(input):
        line = line.replace("\n", "")
        if "|" in line:
            numbers = line.split("|")
            if not numbers[1] in rules:
                rules[numbers[1]] = set()
            rules[numbers[1]].add(numbers[0])
                
            
        else:
            break_point = i
            break

    updates = []
    for j in range(break_point + 1, len(input)):
        updates.append([])
        pages = input[j].replace("\n", "").split(",")
        for page in pages:
            updates[len(updates)-1].append(page)

    return rules, updates


def get_correct_and_incorrect_updates(rules, updates):
    correct_updates = []
    incorrect_updates = []


    for update in updates:  #checks if an upcoming page is within the rule-set of the current page - if so, the update is invalid, else valid
        valid = True
        for i, page in enumerate(update):
            if not page in rules:
                continue
            rule = rules[page]
            for upcoming_page in update[i+1:]:
                if upcoming_page in rule:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            correct_updates.append(update)
        else:
            incorrect_updates.append(update)

    return correct_updates, incorrect_updates


def part_one(input):
    rules, updates = get_rules_and_updates(input)
    correct_updates, _ = get_correct_and_incorrect_updates(rules, updates)
    sum = 0

    for update in correct_updates:
        sum += int(update[len(update)//2])
    
    print("PartOne: " + str(sum))


def part_two(input):
    rules, updates = get_rules_and_updates(input)
    _, incorrect_updates = get_correct_and_incorrect_updates(rules, updates)

    new_updates = []
    for update in incorrect_updates:    #places the update-pages into a new list - for that, checks if at least one of the upcoming pages is inside the current page-rules, if so, the potential index to place is incremented, if not, the page is inserted
        new_update = []
        new_update.append(update[0])

        for page in update[1:]:
            if not page in rules:
                new_update.insert(0, page)
                continue

            rule = rules[page]
            j = 0
            for upcoming_page in new_update:
                if upcoming_page in rule:
                    j += 1
            new_update.insert(j, page)
            j = 0
        new_updates.append(new_update)

    sum = 0
    for update in new_updates:
        sum += int(update[len(update)//2])

    print("PartTwo: " + str(sum))


example = [
    "47|53\n",
    "97|13\n",
    "97|61\n",
    "97|47\n",
    "75|29\n",
    "61|13\n",
    "75|53\n",
    "29|13\n",
    "97|29\n",
    "53|29\n",
    "61|53\n",
    "97|53\n",
    "61|29\n",
    "47|13\n",
    "75|47\n",
    "97|75\n",
    "47|61\n",
    "75|61\n",
    "47|29\n",
    "75|13\n",
    "53|13\n",
    "\n",
    "75,47,61,53,29\n",
    "97,61,53,29,13\n",
    "75,29,13\n",
    "75,97,47,61,53\n",
    "61,13,29\n",
    "97,13,75,29,47\n"
]

data = open("05.txt", "r")
input = data.readlines()
data.close()

part_one(input)
part_two(input)