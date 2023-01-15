import sys
from functools import cmp_to_key
from math import prod


TRUE = -1
EQUAL = 0
FALSE = 1

DIVIDERS = ([[2]], [[6]])


def read_input():
    packets = sys.stdin.read()
    packets = packets.strip()
    packets = packets.replace("\n\n", "\n")
    return packets.split("\n")


def parse_input(packets):
    packets = [eval(packet) for packet in packets]
    return packets


def parse_packets(packets):
    left_packets = [packet for packet in packets[::2]]
    right_packets = [packet for packet in packets[1::2]]
    return zip(left_packets, right_packets)


def compare(left, right):

    def compare_ints(left, right):
        if left < right:
            return TRUE
        if left > right:
            return FALSE
        return EQUAL

    def compare_lists(left, right):
        for i in range(min(len(left), len(right))):
            if (comp := compare(left[i], right[i])) != EQUAL:
                return comp
        if len(left) < len(right):
            return TRUE
        if len(left) > len(right):
            return FALSE
        return EQUAL

    is_int = lambda x: type(x) is int

    if is_int(left) and is_int(right):
        return compare_ints(left, right)

    left = [left] if is_int(left) else left
    right = [right] if is_int(right) else right
    return compare_lists(left, right)


def right_order(left, right):
    return bool(compare(left, right) - 1)


def main(_):
    packets = read_input()
    packets = parse_input(packets)

    packet_pairs = parse_packets(packets)
    pairs_sorted = [right_order(left, right) for left, right in packet_pairs]
    indices_sorted = [
        index + 1
        for index, are_sorted in enumerate(pairs_sorted)
        if are_sorted
    ]
    print(sum(indices_sorted))

    packets.extend(DIVIDERS)
    packets.sort(key=cmp_to_key(compare))
    indices_dividers = [packets.index(divider) + 1 for divider in DIVIDERS]
    print(prod(indices_dividers))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
