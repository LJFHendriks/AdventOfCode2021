import ast
import math
import copy


class Snailfish:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    @classmethod
    def fromList(cls, snail_fish_list):
        if isinstance(snail_fish_list[0], list):
            left = cls.fromList(snail_fish_list[0])
        else:
            left = snail_fish_list[0]
        if isinstance(snail_fish_list[1], list):
            right = cls.fromList(snail_fish_list[1])
        else:
            right = snail_fish_list[1]
        return cls(left, right)

    @classmethod
    def fromString(cls, string):
        return cls.fromList(ast.literal_eval(string))

    def explode(self, root, path=""):
        depth = len(path)

        if isinstance(self.left, Snailfish):
            if self.left.explode(root, path + "0"):
                return True

        if isinstance(self.left, Snailfish):
            if depth >= 3:
                explode(root, path + "0", self.left.left, self.left.right)
                self.left = 0
                return True
        if isinstance(self.right, Snailfish):
            if depth >= 3:
                explode(root, path + "1", self.right.left, self.right.right)
                self.right = 0
                return True

        if isinstance(self.right, Snailfish):
            if self.right.explode(root, path + "1"):
                return True

        return False

    def splits(self):
        if isinstance(self.left, Snailfish):
            if self.left.splits():
                return True

        if not isinstance(self.left, Snailfish):
            if self.left > 9:
                self.left = Snailfish(self.left // 2, int(math.ceil(self.left / 2)))
                return True
        if not isinstance(self.right, Snailfish):
            if self.right > 9:
                self.right = Snailfish(self.right // 2, int(math.ceil(self.right / 2)))
                return True

        if isinstance(self.right, Snailfish):
            if self.right.splits():
                return True

        return False

    def reduce(self):
        while self.explode(self):
            pass

        while self.splits():
            while self.explode(self):
                pass

    def add(self, path, number):
        if len(path) == 0:
            if isinstance(self, Snailfish):
                self.left += number
                return 0
            else:
                print("Error")
        if path[0] == "0":
            if isinstance(self.left, Snailfish):
                return self.left.add(path[1:], number)
            else:
                self.left += number
        elif path[0] == "1":
            if isinstance(self.right, Snailfish):
                return self.right.add(path[1:], number)
            else:
                self.right += number

    def __add__(self, other):
        snailfish = Snailfish(self, other)
        snailfish.reduce()
        return snailfish

    def __str__(self):
        return "[" + str(self.left) + "," + str(self.right) + "]"

    @property
    def magnitude(self):
        if isinstance(self.left, Snailfish):
            left = self.left.magnitude
        else:
            left = self.left
        if isinstance(self.right, Snailfish):
            right = self.right.magnitude
        else:
            right = self.right
        return 3 * left + 2 * right


def explode(root, path, left, right):
    length = len(path)
    number = int(path, 2)
    if int(path, 2) > 0:
        root.add(format(number - 1, f"0{length}b"), left)
    if int(path, 2) < 15:
        root.add(format(number + 1, f"0{length}b"), right)


def get_input(filename="input.txt"):
    with open(filename, "r") as file:
        snail_fish_list = list()
        for line in file:
            snail_fish_list.append(Snailfish.fromString(line))
    return snail_fish_list


def part1():
    snail_fish_list = get_input()

    result = snail_fish_list[0]
    for snail_fish in snail_fish_list[1:]:
        result += snail_fish
    print(result)
    print(result.magnitude)


def part2():
    snail_fish_list = get_input()

    max_magnitude = 0
    for x in snail_fish_list:
        for y in snail_fish_list:
            if x == y:
                continue
            temp_x = copy.deepcopy(x)
            temp_y = copy.deepcopy(y)
            magnitude = (temp_x + temp_y).magnitude
            if magnitude > max_magnitude:
                max_magnitude = magnitude
    print(max_magnitude)


if __name__ == "__main__":
    part1()
    part2()
