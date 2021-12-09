import numpy as np


class LavaTubes:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)
        self.basins = np.array(matrix)

    @classmethod
    def from_file(cls, filename="input.txt"):
        with open(filename, "r") as file:
            matrix = list()
            for line in file:
                matrix.append([int(x) for x in list(line.strip())])
        return cls(np.array(matrix))

    def get_adjacent(self, i, j):
        adjacent = []
        if i > 0:
            adjacent.append(self.matrix[i - 1, j])
        if j > 0:
            adjacent.append(self.matrix[i, j - 1])
        if i < self.matrix.shape[0] - 1:
            adjacent.append(self.matrix[i + 1, j])
        if j < self.matrix.shape[1] - 1:
            adjacent.append(self.matrix[i, j + 1])
        return adjacent

    def get_low_points(self):
        low_points = []
        for i, row in enumerate(self.matrix):
            for j, value in enumerate(row):
                lowest = True
                for adjacent in self.get_adjacent(i, j):
                    if adjacent <= value:
                        lowest = False
                        continue
                if lowest:
                    low_points.append((i, j))
        return low_points

    def get_basin(self, i, j):
        if self.basins[i, j] == 9:
            return 0
        self.basins[i, j] = 9
        total = 1
        if i > 0:
            total += self.get_basin(i - 1, j)
        if j > 0:
            total += self.get_basin(i, j - 1)
        if i < self.basins.shape[0] - 1:
            total += self.get_basin(i + 1, j)
        if j < self.basins.shape[1] - 1:
            total += self.get_basin(i, j + 1)
        return total


def part1():
    lava_tube = LavaTubes.from_file()

    total = 0
    for i, j in lava_tube.get_low_points():
        total += lava_tube.matrix[i, j] + 1

    print(total)


def part2():
    lava_tube = LavaTubes.from_file()

    basins = list()
    for i, j in lava_tube.get_low_points():
        basins.append(lava_tube.get_basin(i, j))

    total = 1
    for i in range(3):
        largest = max(basins)
        basins.remove(largest)
        total *= largest
    print(total)


if __name__ == "__main__":
    part1()
    part2()
