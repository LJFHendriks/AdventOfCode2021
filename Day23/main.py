from copy import deepcopy
from tqdm import tqdm

def get_input(filename="input.txt"):
    with open(filename, "r") as file:
        map = list()
        stack_max = list()
        file.readline()
        for char in file.readline():
            if char == ".":
                map.append(list())
                stack_max.append(0)
        for line in file:
            for i, char in enumerate(line):
                if char in ["A", "B", "C", "D"]:
                    map[i - 1].insert(0, char)
                    stack_max[i - 1] += 1

        for i, value in enumerate(stack_max):
            stack_max[i] = 1 if value == 0 else value

    return map, stack_max

home_room = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

energy_consumption = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000
}


class Position:
    def __init__(self, map, energy=0):
        self.map = map
        self.energy = energy

    def finished(self, max_stack):
        for piece, home in home_room.items():
            if len(self.map[home]) < max_stack[home] or not room_equal(self.map[home], piece):
                return False
        return True


def depth_first(position, max_stack, min_value):
    if position.energy >= min_value:
        return min_value
    if position.finished(max_stack):
        if position.energy < min_value:
            return position.energy
        return min_value
    for i in range(len(position.map)):
        if position.map[i]:
            piece = position.map[i][-1]
            if i == home_room[piece] and room_equal(position.map[i], piece):
                continue
            if max_stack[i] == 1:
                to = home_room[piece]
                if not room_equal(position.map[to], piece):
                    continue
                cost = move(position.map, max_stack, i, to, piece)
                if cost:
                    new_position = deepcopy(position.map)
                    value = new_position[i].pop()
                    new_position[to].append(value)
                    min_value = depth_first(Position(new_position, position.energy + cost), max_stack, min_value)
            else:
                for to in range(len(position.map)):
                    if max_stack[to] > 1:
                        continue
                    if max_stack[to] <= len(position.map[to]):
                        continue
                    cost = move(position.map, max_stack, i, to, piece)
                    if cost:
                        new_position = deepcopy(position.map)
                        value = new_position[i].pop()
                        new_position[to].append(value)
                        min_value = depth_first(Position(new_position, position.energy + cost), max_stack, min_value)
    return min_value


def room_equal(room, piece):
    for roommate in room:
        if roommate != piece:
            return False
    return True


def move(map, max_stack, fron, to, piece):
    total = 0
    to_fron_range = range(fron + 1, to + 1) if to > fron else range(to, fron)
    for i in to_fron_range:
        if max_stack[i] == 1 and len(map[i]) >= max_stack[i]:
            return 0
        total += 1 * energy_consumption[piece]

    if max_stack[fron] > 1:
        total += (max_stack[fron] - len(map[fron]) + 1) * energy_consumption[piece]
    if max_stack[to] > 1:
        total += (max_stack[to] - len(map[to])) * energy_consumption[piece]
    return total



def part1():
    map, stack_max = get_input()

    print(depth_first(Position(map), stack_max, 1000000))


def part2():
    map, stack_max = get_input("input2.txt")

    print(depth_first(Position(map), stack_max, 1000000))


if __name__ == "__main__":
    part1()
    part2()
