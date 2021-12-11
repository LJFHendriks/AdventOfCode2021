import numpy as np


class Octopus:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)
        self.flashed = np.ones(self.matrix.shape)
        self.count = 0

    @classmethod
    def from_file(cls, filename="input.txt"):
        with open(filename, "r") as file:
            matrix = list()
            for line in file:
                matrix.append([int(x) for x in list(line.strip())])
        return cls(matrix)

    def flash(self, i, j):
        self.flashed[i, j] = 0
        self.count += 1

        lower_i = i - 1
        upper_i = i + 2
        lower_j = j - 1
        upper_j = j + 2

        if i == 0:
            lower_i = i
        if j == 0:
            lower_j = j
        if i == self.matrix.shape[0] - 1:
            upper_i = i + 1
        if j == self.matrix.shape[1] - 1:
            upper_j = j + 1

        self.matrix[lower_i:upper_i, lower_j:upper_j] += 1

        for i in range(lower_i, upper_i):
            for j in range(lower_j, upper_j):
                if self.flashed[i, j] == 1 and self.matrix[i, j] > 9:
                    self.flash(i, j)

    def step(self):
        self.matrix += 1

        for i, j in zip(*np.where(self.matrix > 9)):
            if self.flashed[i, j] == 1:
                self.flash(i, j)

        self.matrix = self.matrix * self.flashed
        if np.sum(np.sum(self.flashed)) == 0:
            return True
        self.flashed = np.ones(self.matrix.shape)
        return False



def part1():
    octopus = Octopus.from_file()

    for i in range(100):
        octopus.step()

    print(octopus.count)


def part2():
    octopus = Octopus.from_file()

    all_flashed = False
    i = 0
    while not all_flashed:
        i += 1
        if octopus.step():
            print(i)
            all_flashed = True


if __name__ == "__main__":
    part1()
    part2()
