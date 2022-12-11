import sys


LOWER_PRIORITY = 1
UPPER_PRIORITY = 27


def read_input():
    lines = []
    while (True):
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break
    return lines


def half_split(rucksack):
    half = len(rucksack) // 2
    compartment1 = rucksack[:half]
    compartment2 = rucksack[half:]
    return (compartment1, compartment2)


def find_intruder(rucksack):
    compartment1, compartment2 = rucksack
    for item in compartment1:
        if item in compartment2:
            return item


def get_priority(item):
    if item.islower():
        priority = LOWER_PRIORITY + (ord(item)-ord('a'))
    else:
        priority = UPPER_PRIORITY + (ord(item)-ord('A'))
    return priority


def group_by_elf(rucksacks):
    elfs = []
    for i in range(0, len(rucksacks), 3):
        group = []
        for j in range(0, 3):
            group.append(rucksacks[i+j])
        elfs.append(tuple(group))
    return elfs


def find_badge(group):
    rucksack1, rucksack2, rucksack3 = group
    for item in rucksack1:
        if item in rucksack2 and item in rucksack3:
            return item


def main(_):
    rucksacks = read_input()

    rucksacks_ = [half_split(rucksack) for rucksack in rucksacks]
    intruders = [find_intruder(rucksack) for rucksack in rucksacks_]
    priorities = [get_priority(intruder) for intruder in intruders]
    print(sum(priorities))

    groups = group_by_elf(rucksacks)
    badges = [find_badge(group) for group in groups]
    priorities = [get_priority(badge) for badge in badges]
    print(sum(priorities))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
