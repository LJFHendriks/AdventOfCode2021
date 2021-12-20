import numpy as np

class Enhance:
    def __init__(self, image, padding):
        self.padding = padding

        self.original = np.pad(image, self.padding)

        self.target = np.zeros(self.original.shape, dtype=int)

    def enhance(self, enhance_string):
        for i in range(self.original.shape[0]):
            for j in range(self.original.shape[1]):
                temp = np.take(self.original, range(i-1, i+2), axis=0, mode="wrap")
                str = np.array2string(np.take(temp, range(j-1, j+2), axis=1, mode='wrap').flatten(), separator="")
                index = int(str[1:-1], 2)
                self.target[i, j] = 1 if enhance_string[index] == "#" else 0
        self.original = self.target
        self.target = np.zeros(self.original.shape, dtype=int)

    def lit_pixels(self):
        return np.sum(np.sum(self.original))

    def __str__(self):
        string = ""
        for line in self.original:
            for char in line:
                if char == 1:
                    string += "#"
                else:
                    string += "."
            string += "\n"
        return string


def get_input(filename="input.txt"):
    with open(filename, "r") as file:
        enhance_string = ""
        next_line = file.readline()
        while next_line != "\n":

            enhance_string += next_line.strip()
            next_line = file.readline()

        matrix = []
        for line in file:
            matrix.append([1 if x == "#" else 0 for x in line.strip()])
    return np.array(matrix), enhance_string


def part1():
    image, enhance_string = get_input()

    enhance = Enhance(image, 3)
    for i in range(2):
        enhance.enhance(enhance_string)
    print(enhance.lit_pixels())





def part2():
    image, enhance_string = get_input()

    enhance = Enhance(image, 51)
    for i in range(50):
        enhance.enhance(enhance_string)
    print(enhance.lit_pixels())

if __name__ == "__main__":
    part1()
    part2()
