from tqdm import tqdm
import numpy as np


def get_input(filename="input.txt"):
    with open(filename, "r") as file:
        operations = list()
        for line in file:
            operations.append(line.split())
    return ALU(operations)


letter_2_number = {
    "w": 0,
    "x": 1,
    "y": 2,
    "z": 3
}


class ALU:
    def __init__(self, operations):
        self.operations = operations
        self.states = {
            (0, 0, 0, 0): "0"
        }

    def search_lowest(self):
        i = 0
        while i < len(self.operations):
            new_states = {}
            states = self.states.keys()
            model_numbers = self.states.values()
            states = np.array(list(states), dtype=int)
            while i < len(self.operations) and self.operations[i][0] != "inp":
                operation = self.operations[i]
                state = apply_operation(states, operation, operation_dict[operation[0]])
                print(i)
                i += 1
            for state, model_number in zip(states, model_numbers):
                new_state = tuple(state)
                if int(model_number) <= int(new_states.get(new_state, 1e20)):
                    new_states[new_state] = model_number
            self.states = new_states
            if i < len(self.operations):
                new_states = {}
                states = self.states.keys()
                model_numbers = self.states.values()
                states = np.array(list(states), dtype=int)
                for state, model_number in zip(states, model_numbers):
                    for j in range(1, 10):
                        state[letter_2_number[self.operations[i][1]]] = j
                        new_state = tuple(state)
                        if int(model_number + str(j)) < int(new_states.get(new_state, 1e20)):
                            new_states[new_state] = model_number + str(j)
                self.states = new_states
                i += 1

    def search_highest(self):
        i = 0
        while i < len(self.operations):
            new_states = {}
            states = self.states.keys()
            model_numbers = self.states.values()
            states = np.array(list(states), dtype=int)
            while i < len(self.operations) and self.operations[i][0] != "inp":
                operation = self.operations[i]
                state = apply_operation(states, operation, operation_dict[operation[0]])
                print(i)
                i += 1
            for state, model_number in zip(states, model_numbers):
                new_state = tuple(state)
                if int(model_number) >= int(new_states.get(new_state, 0)):
                    new_states[new_state] = model_number
            self.states = new_states
            if i < len(self.operations):
                new_states = {}
                states = self.states.keys()
                model_numbers = self.states.values()
                states = np.array(list(states), dtype=int)
                for state, model_number in zip(states, model_numbers):
                    for j in range(1, 10):
                        state[letter_2_number[self.operations[i][1]]] = j
                        new_state = tuple(state)
                        if int(model_number + str(j)) > int(new_states.get(new_state, 0)):
                            new_states[new_state] = model_number + str(j)
                self.states = new_states
                i += 1



operation_dict = {
    "add": lambda x, y: x + y,
    "mul": lambda x, y: x * y,
    "div": lambda x, y: x // y,
    "mod": lambda x, y: x % y,
    "eql": lambda x, y: (x == y).astype(int)
}


def apply_operation(states, operation, operator):
    if operation[2] in letter_2_number.keys():
        states[:, letter_2_number[operation[1]]] = operator(states[:, letter_2_number[operation[1]]],
                                                            states[:, letter_2_number[operation[2]]])
    else:
        states[:, letter_2_number[operation[1]]] = operator(states[:, letter_2_number[operation[1]]],
                                                            int(operation[2]))
    return states


def part1():
    alu = get_input()

    alu.search_highest()

    max_model_number = 0
    for state, model_number in alu.states.items():
        if state[3] == 0 and int(model_number) > max_model_number:
            max_model_number = int(model_number)

    print(max_model_number)


def part2():
    alu = get_input()

    alu.search_lowest()

    min_model_number = int(1e20)
    for state, model_number in alu.states.items():
        if state[3] == 0 and int(model_number) < min_model_number:
            min_model_number = int(model_number)

    print(min_model_number)


if __name__ == "__main__":
    part1()
    part2()
