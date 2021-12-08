import numpy as np

alphabet = {"a", "b", "c", "d", "e", "f", "g"}

display_dict = {
    0: {"a", "b", "c", "e", "f", "g"},
    1: {"c", "f"},
    2: {"a", "c", "d", "e", "g"},
    3: {"a", "c", "d", "f", "g"},
    4: {"b", "c", "d", "f"},
    5: {"a", "b", "d", "f", "g"},
    6: {"a", "b", "d", "e", "f", "g"},
    7: {"a", "c", "f"},
    8: {"a", "b", "c", "d", "e", "f", "g"},
    9: {"a", "b", "c", "d", "f", "g"}
}


class Display:
    def __init__(self, input, output):
        self.input = [set(list(x)) for x in input]
        self.output = [set(list(x)) for x in output]
        self.map = dict()
        self.inverted_map = dict()

    def count_easy(self):
        # count occurrences of 1, 4, 7, 8
        total = 0
        for out in self.output:
            if len(out) in [2, 3, 4, 7]:
                total += 1
        return total

    def deduct(self):
        for ins in self.input:
            if len(ins) == 2:
                self.map[1] = ins
            if len(ins) == 3:
                self.map[7] = ins
            if len(ins) == 4:
                self.map[4] = ins
            if len(ins) == 7:
                self.map[8] = ins

        for ins in self.input:
            if len(ins) == 5:
                if self.map[7].issubset(ins):
                    self.map[3] = ins
                elif (self.map[4] - self.map[1]).issubset(ins):
                    self.map[5] = ins
                else:
                    self.map[2] = ins

        for ins in self.input:
            if len(ins) == 6:
                if (self.map[2] - self.map[3]).isdisjoint(ins):
                    self.map[9] = ins
                elif (self.map[3] - self.map[5]).isdisjoint(ins):
                    self.map[6] = ins
                else:
                    self.map[0] = ins

        self.inverted_map = {frozenset(v): k for k, v in self.map.items()}

    def decode(self):
        total = 0
        for i, value in enumerate(self.output):
            total += 10 ** (3 - i) * self.inverted_map[frozenset(value)]
        return total


def get_input():
    with open("input.txt", "r") as file:
        displays = list()
        for line in file:
            output = line.replace(" | ", " ").split()
            displays.append(Display(output[0:10], output[10:14]))
    return displays


def part1():
    displays = get_input()
    total = 0
    for display in displays:
        total += display.count_easy()
    print(total)


def part2():
    displays = get_input()
    total = 0
    for display in displays:
        display.deduct()
        total += display.decode()

    print(total)


if __name__ == "__main__":
    part1()
    part2()
