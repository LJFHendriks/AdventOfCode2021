import numpy as np




def get_fish():
    with open("input.txt", "r") as file:
        fish_list = [int(x) for x in file.read().split(",")]
    return fish_list

def part1():
    fish_list = get_fish()
    for i in range(80):
        print(i)
        new_fish_list = list()
        for fish in fish_list:
            if fish == 0:
                new_fish_list.extend([6, 8])
            else:
                new_fish_list.append(fish-1)
        fish_list = new_fish_list

    print(len(new_fish_list))



def part2():
    fish_list = np.array(get_fish())
    unique, counts = np.unique(fish_list, return_counts=True)
    fish_dict = dict(zip(unique, counts))
    for i in range(256):
        print(i)
        new_fish_dict = dict()
        for key, value in fish_dict.items():
            if key == 0:
                new_fish_dict[6] = new_fish_dict.setdefault(6, 0) + value
                new_fish_dict[8] = new_fish_dict.setdefault(8, 0) + value
            else:
                new_fish_dict[key - 1] = new_fish_dict.setdefault(key - 1, 0) + value
        fish_dict = new_fish_dict

    total = 0
    for key, value in fish_dict.items():
        total += value
    print(total)


if __name__ == "__main__":
    part1()
    part2()
