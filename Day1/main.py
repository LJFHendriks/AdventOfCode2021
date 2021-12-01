import numpy as np


def part1():
    depths = np.loadtxt("input.txt")
    increase = np.sum(depths[1:] > depths[:-1])

    print(f"The depth increases on {increase} occasions.")

def part2():
    depths = np.loadtxt("input.txt")
    depths3sum = depths[:-2] + depths[1:-1] + depths[2:]
    increase = np.sum(depths3sum[1:] > depths3sum[:-1])

    print(f"The 3 sum depth increases on {increase} occasions.")


if __name__ == "__main__":
    part1()
    part2()
