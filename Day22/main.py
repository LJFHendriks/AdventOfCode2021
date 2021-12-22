import numpy as np
from tqdm import tqdm

def get_input(filename="input.txt"):
    with open(filename, "r") as file:
        on_off = list()
        cubes = list()
        for line in file:
            split_line = line.replace(" x=", "..").replace(",y=", "..").replace(",z=", "..").split("..")
            on_off.append(1 if split_line[0] == "on" else -1)
            cubes.append([int(x) for x in split_line[1:]])
    return np.array(cubes, dtype='int64'), on_off


class Reactor:
    def __init__(self, size):
        self.size = size
        self.on = np.zeros((2 * self.size + 1, 2 * self.size + 1, 2 * self.size + 1), dtype='int64')

    def turn_on(self, cubes, on_off):
        for i, cube in enumerate(self.shift(cubes)):
            if np.any(cube < 0) or np.any(cube > 2 * self.size):
                continue
            if on_off[i] == 1:
                self.on[cube[0]:cube[1]+1, cube[2]:cube[3]+1, cube[4]:cube[5]+1] = 1
            else:
                self.on[cube[0]:cube[1]+1, cube[2]:cube[3]+1, cube[4]:cube[5]+1] = 0

    def shift(self, cubes):
        return cubes + self.size

    @property
    def count_on(self):
        return np.sum(np.sum(np.sum(self.on)))


def part1():
    cubes, on_off = get_input()
    reactor = Reactor(50)
    reactor.turn_on(cubes, on_off)
    print(reactor.count_on)


def turn_on(cubes, on_offs):
    better_cubes = list()
    better_on_offs = list()
    for cube, on_off in tqdm(zip(cubes, on_offs)):
        for better_cube, better_on_off in zip(better_cubes.copy(), better_on_offs.copy()):
            intersection = better_cube + cube
            if intersection.size > 0:
                better_cubes.append(intersection)
                better_on_offs.append(-1 * better_on_off)
        if on_off == 1:
            better_cubes.append(cube)
            better_on_offs.append(on_off)
    return size(better_cubes, better_on_offs)


def size(cubes, on_offs):
    total = 0
    for cube, on_off in zip(cubes, on_offs):
        total += on_off * cube.size
    return total


class Cube:
    def __init__(self, cube):
        self.x1 = cube[0]
        self.x2 = cube[1]

        self.y1 = cube[2]
        self.y2 = cube[3]

        self.z1 = cube[4]
        self.z2 = cube[5]

    @property
    def size(self):
        return max(self.x2 - self.x1, 0) * max(self.y2 - self.y1, 0) * max(self.z2 - self.z1, 0)

    def __add__(self, other):
        return Cube([max(self.x1, other.x1), min(self.x2, other.x2),
                     max(self.y1, other.y1), min(self.y2, other.y2),
                     max(self.z1, other.z1), min(self.z2, other.z2)])

    def __str__(self):
        return f"[x: {self.x1},{self.x2}; y: {self.y1},{self.y2}; z: {self.z1},{self.z2};]"


def part2():
    cubes, on_offs = get_input()

    cubes[:, 1] += 1
    cubes[:, 3] += 1
    cubes[:, 5] += 1
    cubes = [Cube(cube) for cube in cubes]
    print(turn_on(cubes, on_offs))


if __name__ == "__main__":
    part1()
    part2()
