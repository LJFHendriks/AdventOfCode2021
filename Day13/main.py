import numpy as np


class TransPaper:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)

    def fold_y(self, line):
        top = self.matrix[:line, :]
        bottom = self.matrix[:line:-1, :]

        if top.shape[0] > bottom.shape[0]:
            bottom = np.vstack((np.zeros((top.shape[0] - bottom.shape[0], bottom.shape[1])), bottom))
        if top.shape[0] < bottom.shape[0]:
            top = np.vstack((np.zeros((bottom.shape[0] - top.shape[0], top.shape[1])), top))
        self.matrix = top + bottom

    def fold_x(self, line):
        left = self.matrix[:, :line]
        right = self.matrix[:, :line:-1]

        if left.shape[1] > right.shape[1]:
            right = np.hstack((np.zeros((right.shape[0], left.shape[1] - right.shape[1])), right))
        if left.shape[1] < right.shape[1]:
            left = np.hstack((np.zeros((left.shape[0], right.shape[1] - left.shape[1])), left))
        self.matrix = left + right

    def count_dots(self):
        return np.count_nonzero(self.matrix)

    def __str__(self):
        string = ""
        for line in self.matrix:
            for char in line:
                if char > 0:
                    string += "█"
                else:
                    string += " "
            string += "\n"
        return string


def get_input(filename="input.txt"):
    with open(filename, "r") as file:
        coords_x = list()
        coords_y = list()
        folds = list()

        for line in file:
            if line.startswith("fold along "):
                type = line[11]
                position = line.strip()[13:]
                folds.append((type, int(position)))
            elif line == "\n":
                continue
            else:
                x, y = line.strip().split(",")
                coords_x.append(int(x))
                coords_y.append(int(y))
    matrix = np.zeros((max(coords_y) + 1, max(coords_x) + 1))
    for x, y in zip(coords_x, coords_y):
        matrix[y, x] += 1
    return TransPaper(matrix), folds


def part1():
    trans_paper, folds = get_input()

    for type, position in folds[0:1]:
        if type == "x":
            trans_paper.fold_x(position)
        elif type == "y":
            trans_paper.fold_y(position)
    print(trans_paper.count_dots())


def part2():
    trans_paper, folds = get_input()

    for type, position in folds:
        if type == "x":
            trans_paper.fold_x(position)
        elif type == "y":
            trans_paper.fold_y(position)

    print(trans_paper)


if __name__ == "__main__":
    part1()
    part2()
