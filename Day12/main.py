def find_paths(position, graph, visited, double_up):
    if position == "end":
        return 1
    total = 0
    for next in graph.get(position, []):
        if next.isupper() or not next in visited:
            new_visited = visited.copy()
            new_visited.append(next)
            total += find_paths(next, graph, new_visited, double_up)
        elif next not in ["start", "end"] and not double_up:
            total += find_paths(next, graph, visited, True)
    return total


def get_input(filename="input.txt"):
    with open(filename, "r") as file:
        graph = dict()
        for line in file:
            x, y = line.strip().split("-")
            graph.setdefault(x, []).append(y)
            graph.setdefault(y, []).append(x)
    return graph


def part1():
    graph = get_input()
    print(find_paths("start", graph, ["start"], True))


def part2():
    graph = get_input()
    print(find_paths("start", graph, ["start"], False))


if __name__ == "__main__":
    part1()
    part2()
