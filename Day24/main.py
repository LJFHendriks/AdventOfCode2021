from tqdm import tqdm

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
            (0, 0, 0, 0): ""
        }

    def search_lowest(self):
        for operation in tqdm(self.operations):
            new_states = {}
            match operation[0]:
                case "inp":
                    for state, model_number in self.states.items():
                        for i in range(1, 10):
                            new_state = list(state)
                            new_state[letter_2_number[operation[1]]] = i
                            new_state = tuple(new_state)
                            if int(model_number + str(i)) > int(new_states.get(new_state, 0)):
                                new_states[new_state] = model_number + str(i)
                case "add":
                    for state, model_number in self.states.items():
                        new_state = apply_operation(state, operation, lambda x, y: x + y)
                        if int(model_number) > int(new_states.get(new_state, 0)):
                            new_states[new_state] = model_number
                case "mul":
                    for state, model_number in self.states.items():
                        new_state = apply_operation(state, operation, lambda x, y: x * y)
                        if int(model_number) > int(new_states.get(new_state, 0)):
                            new_states[new_state] = model_number
                case "div":
                    for state, model_number in self.states.items():
                        new_state = apply_operation(state, operation, lambda x, y: x // y)
                        if int(model_number) > int(new_states.get(new_state, 0)):
                            new_states[new_state] = model_number
                case "mod":
                    for state, model_number in self.states.items():
                        new_state = apply_operation(state, operation, lambda x, y: x % y)
                        if int(model_number) > int(new_states.get(new_state, 0)):
                            new_states[new_state] = model_number
                case "eql":
                    for state, model_number in self.states.items():
                        new_state = apply_operation(state, operation, lambda x, y: int(x == y))
                        if int(model_number) > int(new_states.get(new_state, 0)):
                            new_states[new_state] = model_number
            self.states = new_states


def apply_operation(state, operation, operator):
    new_state = list(state)
    if operation[2] in letter_2_number.keys():
        new_state[letter_2_number[operation[1]]] = operator(new_state[letter_2_number[operation[1]]],
                                                            new_state[letter_2_number[operation[2]]])
    else:
        new_state[letter_2_number[operation[1]]] = operator(new_state[letter_2_number[operation[1]]],
                                                           int(operation[2]))
    return tuple(new_state)


def part1():
    alu = get_input()

    alu.search_lowest()

    print(min([int(x) for x in alu.states.values()]))


def part2():
    cubes, on_offs = get_input()


if __name__ == "__main__":
    part1()
    # part2()
