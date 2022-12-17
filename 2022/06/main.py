import sys


PKT_WINDOW = 4
MSG_WINDOW = 14


def parse_arguments(args):
    if len(args) >= 2:
        return int(args[1])
    return 0


def read_input():
    lines = []
    while (True):
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break
    return lines


def window_split(signal, window):
    return [signal[i:i+window] for i in range(len(signal))]


def is_marker(string):
    unique = set(string)
    return len(string) == len(unique)


def marker(ls):
    window = len(ls[0])

    markers = [is_marker(string) for string in ls]
    index = markers.index(True)

    return window + index


def main(args):
    num = parse_arguments(args)
    signal = read_input()[num]

    packets = window_split(signal, PKT_WINDOW)
    print(marker(packets))

    messages = window_split(signal, MSG_WINDOW)
    print(marker(messages))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
