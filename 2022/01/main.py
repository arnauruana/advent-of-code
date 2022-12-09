import sys


def read_input_grouped():
    elf_calories = []
    sum_calories = 0
    while (True):
        try:
            calories = input()
            if calories == '':
                elf_calories.append(sum_calories)
                sum_calories = 0
            else:
                sum_calories += int(calories)
        except EOFError:
            elf_calories.append(sum_calories)
            break
    return elf_calories


def main(_):
    calories_elf = read_input_grouped()

    print(max(calories_elf))

    calories_elf.sort(reverse=True)
    print(sum(calories_elf[:3]))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
