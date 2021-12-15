import numpy as np


def get_input(filename="input.txt"):
    with open(filename, "r") as file:
        matrix = list()
        for line in file:
            matrix.append([int(x) for x in list(line.strip())])
    return np.array(matrix)


class Dijkstra:
    def __init__(self, matrix):
        self.matrix = matrix
        self.dist = np.full(matrix.shape, np.iinfo(np.int32(10)).max)
        self.dist[0, 0] = 0
        self.Q = np.ones(matrix.shape)

    def shortest_path(self):
        while np.sum(np.sum(self.Q)) > 0:
            cover = np.where(self.Q == 1, self.dist, np.iinfo(np.int32(10)).max)
            i, j = np.unravel_index(cover.argmin(), cover.shape)
            self.Q[i, j] = 0

            if i == matrix.shape[0] - 1 and j == matrix.shape[1] - 1:
                break

            for adj_i, adj_j in self.get_adjacents(i, j):
                alt = self.dist[i, j] + self.matrix[adj_i, adj_j]
                if alt < self.dist[adj_i, adj_j]:
                    self.dist[adj_i, adj_j] = alt
        return self.dist[matrix.shape[0] - 1, matrix.shape[1] - 1]

    def get_adjacents(self, i, j):
        adjacents = list()
        if i > 0:
            if self.Q[i - 1, j] == 1:
                adjacents.append((i - 1, j))
        if j > 0:
            if self.Q[i, j - 1] == 1:
                adjacents.append((i, j - 1))
        if i < self.matrix.shape[0] - 1:
            if self.Q[i + 1, j] == 1:
                adjacents.append((i + 1, j))
        if j < self.matrix.shape[1] - 1:
            if self.Q[i, j + 1] == 1:
                adjacents.append((i, j + 1))
        return adjacents


def part1():
    short_path = Dijkstra(matrix)
    print(short_path.shortest_path())


def part2():
    short_path = Dijkstra(matrix)
    print(short_path.shortest_path())


if __name__ == "__main__":
    matrix = get_input()
    part1()
    ini_matrix = matrix.copy()
    for i in range(1, 5):
        matrix = np.hstack((matrix, ini_matrix + i))
    ini_matrix = matrix.copy()
    for j in range(1, 5):
        matrix = np.vstack((matrix, ini_matrix + j))
    matrix = (matrix - 1) % 9 + 1

    part2()
