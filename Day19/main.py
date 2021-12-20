import numpy as np
from numpy.linalg import matrix_power


class Map:
    def __init__(self):
        self.beacons = np.zeros((0, 3), dtype=int)
        self.scanners = np.zeros((1, 3), dtype=int)

    def add_beacons(self, beacons):
        for beacon in beacons:
            if self.beacons.shape[0] == 0:
                self.beacons = np.vstack((self.beacons, beacon))
            elif beacon.tolist() not in self.beacons.tolist():
                self.beacons = np.vstack((self.beacons, beacon))

    def add_scanner(self, scanner):
        self.scanners = np.vstack((self.scanners, scanner))

    def number_of_beacons(self):
        return self.beacons.shape[0]

    def in_map_range(self, beacon):
        for scanner in self.scanners:
            if in_range(scanner, beacon):
                return True
        return False


def in_range(scanner, beacon):
    for i in range(3):
        if beacon[i] < scanner[i] - 1000 or beacon[i] > scanner[i] + 1000:
            return False
    return True


def get_input(filename="input.txt"):
    with open(filename, "r") as file:
        scanners = list()
        for line in file:
            if line[0:12] == "--- scanner ":
                scanner = list()
            elif line == "\n":
                scanners.append(np.array(scanner, dtype=int))
            else:
                scanner.append([int(x) for x in line.split(",")])
        scanners.append(np.array(scanner, dtype=int))
    return scanners


def orientations(beacon_matrix):
    matrix_orientations = list()
    r_x = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]], dtype=int)
    r_y = np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]], dtype=int)
    r_z = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]], dtype=int)
    for i, j in [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (0, 3)]:
        for h in range(4):
            matrix_orientations.append(beacon_matrix @ (matrix_power(r_x, i) @ matrix_power(r_y, j) @ matrix_power(r_z, h)).transpose())
    return matrix_orientations


def compare_scanner(map, scanner):
    scanner_orientations = orientations(scanner)
    for scanner_orientation in scanner_orientations:
        for row in scanner_orientation:
            for beacon in map.beacons:
                shift = beacon - row
                shifted_scanner = scanner_orientation + shift

                total = 0
                for shifted_row in shifted_scanner:
                    if shifted_row.tolist() in map.beacons.tolist():
                        total += 1
                    else:
                        if map.in_map_range(shifted_row):
                            break
                    if total >= 12:
                        map.add_beacons(shifted_scanner)
                        map.add_scanner(shift)
                        return True
    return False


def part1():
    scanners = get_input()
    map = Map()
    map.add_beacons(scanners.pop(0))
    while len(scanners) > 0:
        scanner = scanners.pop(0)
        if not compare_scanner(map, scanner):
            scanners.append(scanner)
    print(map.number_of_beacons())


def part2():
    scanners = get_input()
    map = Map()
    map.add_beacons(scanners.pop(0))
    while len(scanners) > 0:
        scanner = scanners.pop(0)
        if not compare_scanner(map, scanner):
            scanners.append(scanner)

    max_distance = 0
    for scanner in map.scanners:
        for scanner2 in map.scanners:
            distance = np.sum(np.abs(scanner - scanner2))
            if distance > max_distance:
                max_distance = distance

    print(max_distance)


if __name__ == "__main__":
    part1()
    part2()
