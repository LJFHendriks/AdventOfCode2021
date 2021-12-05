import numpy as np




def get_lines():
    with open("input.txt", "r") as file:
        lines = []
        for line in file:
            lines.append([int(x) for x in line.replace(" -> ", ",").split(",")])
    return np.array(lines)

def part1():
    lines = get_lines()
    coverage = np.zeros((np.max(lines[:, (0, 2)]) + 1, np.max(lines[:, (1, 3)]) + 1))

    for line in lines:
        if line[0] != line[2] and line[1] != line[3]:
            continue
        for i in range(min(line[0], line[2]), max(line[0], line[2]) + 1):
            for j in range(min(line[1], line[3]), max(line[1], line[3]) + 1):
                coverage[j, i] += 1
    print(np.sum(coverage >= 2))



def part2():
    lines = get_lines()
    coverage = np.zeros((np.max(lines[:, (0, 2)]) + 1, np.max(lines[:, (1, 3)]) + 1))

    for line in lines:

        step_x = int((line[2] - line[0]) / max(np.abs(line[2] - line[0]), np.abs(line[3] - line[1])))
        step_y = int((line[3] - line[1]) / max(np.abs(line[2] - line[0]), np.abs(line[3] - line[1])))
        x = line[0]
        y = line[1]
        while x != line[2] or y != line[3]:
            coverage[y, x] += 1
            x += step_x
            y += step_y
        coverage[y, x] += 1
    print(np.sum(coverage >= 2))


if __name__ == "__main__":
    part1()
    part2()
