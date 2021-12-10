import numpy as np
from collections import deque


matching_brackets = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}

points_errors = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

points_missing = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}

class Syntax:
    def __init__(self, string):
        self.string = string
        self.stack = deque()
        self.comp_score = -1

    def find_error(self):
        for char in self.string:
            if char in matching_brackets.keys():
                if matching_brackets[char] != self.stack.pop():
                    return points_errors[char]
            else:
                self.stack.append(char)
        return 0

    def compute_comp_score(self):
        if self.find_error() == 0:
            total = 0
            while self.stack:
                total *= 5
                total += points_missing[self.stack.pop()]
            self.comp_score = total

    def __lt__(self, other):
        return self.comp_score < other.comp_score


def get_input():
    with open("input.txt", "r") as file:
        syntax_lines = list()
        for line in file:
            syntax_lines.append(Syntax(line.strip()))
    return syntax_lines


def part1():
    syntax_lines = get_input()

    total = 0
    for syntax in syntax_lines:
        total += syntax.find_error()

    print(total)


def part2():
    syntax_lines = get_input()

    for syntax in syntax_lines:
        syntax.compute_comp_score()

    syntax_lines = list(filter(lambda s: s.comp_score >= 0, syntax_lines))

    syntax_lines.sort()

    print(syntax_lines[len(syntax_lines) // 2].comp_score)


if __name__ == "__main__":
    part1()
    part2()
