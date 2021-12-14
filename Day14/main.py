from collections import Counter
from tqdm import tqdm

class Polymerization:
    def __init__(self, polymer):
        self.polymer = polymer

    def step(self, pairs):
        result = ""
        for i in range(len(self.polymer)-1):
            if self.polymer[i] + self.polymer[i + 1] in pairs:
                result += pairs.get(self.polymer[i] + self.polymer[i + 1])
        result += self.polymer[-1]
        self.polymer = result
        return self.polymer


def get_input(filename="input.txt"):
    with open(filename, "r") as file:

        polymer = Polymerization(file.readline().strip())
        file.readline()
        pairs = dict()
        for line in file:
            key, value = line.strip().split(" -> ")
            pairs[key] = key[0] + value
    return polymer, pairs


def part1():
    polymer, pairs = get_input()


    for i in range(10):
        polymer.step(pairs)
    counts = Counter(polymer.polymer)
    print(max(counts.values()) - min(counts.values()))


def part2():
    polymer, pairs = get_input()

    pairs10 = dict()
    for key in pairs.keys():
        key_polymer = Polymerization(key)
        for i in range(10):
            key_polymer.step(pairs)
        pairs10[key] = key_polymer.polymer[:-1]

    pairs20 = dict()
    counts20 = dict()
    for key in pairs10.keys():
        key_polymer = Polymerization(key)
        for i in range(2):
            key_polymer.step(pairs10)
        pairs20[key] = key_polymer.polymer[:-1]
        counts20[key] = Counter(key_polymer.polymer[:-1])

    polymer.step(pairs20)

    result = Counter()
    for i in tqdm(range(len(polymer.polymer) - 1)):
        result += counts20.get(polymer.polymer[i] + polymer.polymer[i + 1])
    result += Counter(polymer.polymer[-1])

    print(max(result.values()) - min(result.values()))


if __name__ == "__main__":
    part1()
    part2()
