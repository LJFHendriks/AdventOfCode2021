from collections import Counter
from tqdm import tqdm

class Probe:
    def __init__(self, x_vel, y_vel, target):
        self.target = target

        self.x_vel = x_vel
        self.y_vel = y_vel

    def fly(self):
        x = 0
        y = 0
        while x <= self.target[1] and y >= self.target[2]:
            x += self.x_vel
            y += self.y_vel

            if self.x_vel > 0:
                self.x_vel -= 1
            self.y_vel -= 1

            if self.target[0] <= x <= self.target[1] and self.target[2] <= y <= self.target[3]:
                return True
        return False



def get_input(filename="input.txt"):
    with open(filename, "r") as file:

        target = [int(x) for x in file.readline().replace("target area: x=", "").replace(", y=", "..").split("..")]
    return target


def part1():
    target = get_input()

    max_height = 0
    for y_vel in range(120):
        for x_vel in range(target[1]):
            if Probe(x_vel, y_vel, target).fly():
                max_height = y_vel*(y_vel + 1) // 2
                break
    print(max_height)



def part2():
    target = get_input()

    total = 0
    for y_vel in range(target[2], 120):
        for x_vel in range(target[1]+1):
            if Probe(x_vel, y_vel, target).fly():
                total += 1
    print(total)


if __name__ == "__main__":
    part1()
    part2()
