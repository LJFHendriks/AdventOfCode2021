import numpy as np


class Bingo:
    def __init__(self, board):
        self.board = np.array(board)
        self.checked = np.zeros(self.board.shape)
        self.last = -1

    def update(self, number):
        location = np.where(self.board == number)
        for x, y in zip(location[0], location[1]):
            self.checked[x, y] = 1
        if self.complete():
            return int(number * sum(sum((self.board * (1 - self.checked)))))
        return -1

    def complete(self):
        if 5 in np.sum(self.checked, axis=0):
            return True
        if 5 in np.sum(self.checked, axis=1):
            return True
        return False


def get_boards():
    with open("input.txt", "r") as file:
        callouts = [int(x) for x in file.readline().split(",")]
        file.readline()
        board = list()
        bingo_boards = list()
        for index, line in enumerate(file):
            if index % 6 == 5:
                bingo_boards.append(Bingo(board))
                board = list()
            else:
                board.append([int(x) for x in line.split()])
        bingo_boards.append(Bingo(board))
    return callouts, bingo_boards


def part1():
    callouts, bingo_boards = get_boards()

    stop = False
    for call in callouts:
        for board in bingo_boards:
            result = board.update(call)
            if result != -1:
                print(result)
                stop = True
                break

        if stop == True:
            break


def part2():
    callouts, bingo_boards = get_boards()

    stop = False
    for call in callouts:
        removed = 0
        for i in range(len(bingo_boards)):
            result = bingo_boards[i - removed].update(call)
            if result != -1:
                if len(bingo_boards) == 1:
                    print(result)
                    stop = True
                    break
                else:
                    bingo_boards.remove(bingo_boards[i - removed])
                    removed += 1
        if stop:
            break


if __name__ == "__main__":
    part1()
    part2()
