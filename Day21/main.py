def get_input(filename="input.txt"):
    with open(filename, "r") as file:
        start_pos_1 = file.readline().replace("Player 1 starting position: ", "").strip()
        start_pos_2 = file.readline().replace("Player 2 starting position: ", "").strip()
    return int(start_pos_1), int(start_pos_2)


class DiracDice:
    def __init__(self, start_pos_1, start_pos_2):
        self.pos_1 = start_pos_1
        self.pos_2 = start_pos_2
        self.score_1 = 0
        self.score_2 = 0
        self.det_die = 1
        self.die_rolls = 0

    def move_1(self, roll):
        self.pos_1 = (self.pos_1 + roll - 1) % 10 + 1
        self.score_1 += self.pos_1
        if self.score_1 >= 1000:
            return True
        return False

    def move_2(self, roll):
        self.pos_2 = (self.pos_2 + roll - 1) % 10 + 1
        self.score_2 += self.pos_2
        if self.score_2 >= 1000:
            return True
        return False

    def roll(self):
        total = 0
        for i in range(3):
            total += self.det_die
            self.det_die = self.det_die % 100 + 1
            self.die_rolls += 1
        return total

    def game(self):
        winner = False
        last_player = 2
        while not winner:
            if last_player == 2:
                winner = self.move_1(self.roll())
                last_player = 1
            else:
                winner = self.move_2(self.roll())
                last_player = 2
        if last_player == 1:
            return self.die_rolls * self.score_2
        else:
            return self.die_rolls * self.score_1

class DiracDice:
    def __init__(self, start_pos_1, start_pos_2):
        self.pos_1 = start_pos_1
        self.pos_2 = start_pos_2
        self.score_1 = 0
        self.score_2 = 0
        self.det_die = 1
        self.die_rolls = 0

    def move_1(self, roll):
        self.pos_1 = (self.pos_1 + roll - 1) % 10 + 1
        self.score_1 += self.pos_1
        if self.score_1 >= 1000:
            return True
        return False

    def move_2(self, roll):
        self.pos_2 = (self.pos_2 + roll - 1) % 10 + 1
        self.score_2 += self.pos_2
        if self.score_2 >= 1000:
            return True
        return False

    def roll(self):
        total = 0
        for i in range(3):
            total += self.det_die
            self.det_die = self.det_die % 100 + 1
            self.die_rolls += 1
        return total

    def game(self):
        winner = False
        last_player = 2
        while not winner:
            if last_player == 2:
                winner = self.move_1(self.roll())
                last_player = 1
            else:
                winner = self.move_2(self.roll())
                last_player = 2
        if last_player == 1:
            return self.die_rolls * self.score_2
        else:
            return self.die_rolls * self.score_1

roll_count = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1
}

class QuantumDiracDice:
    def __init__(self, start_pos_1, start_pos_2):
        self.states = {(start_pos_1, 0, start_pos_2, 0): 1}
        self.universes_1_win = 0
        self.universes_2_win = 0

    def move_1(self):
        new_states = dict()
        for key, value in self.states.items():
            for i in range(3, 10):
                pos_1, score_1, pos_2, score_2 = key
                pos_1 = (pos_1 + i - 1) % 10 + 1
                score_1 += pos_1
                if score_1 >= 21:
                    self.universes_1_win += roll_count[i] * value
                else:
                    new_states[(pos_1, score_1, pos_2, score_2)] = new_states.setdefault(
                        (pos_1, score_1, pos_2, score_2), 0) + roll_count[i] * value
        self.states = new_states

    def move_2(self):
        new_states = dict()
        for key, value in self.states.items():
            for i in range(3, 10):
                pos_1, score_1, pos_2, score_2 = key
                pos_2 = (pos_2 + i - 1) % 10 + 1
                score_2 += pos_2
                if score_2 >= 21:
                    self.universes_2_win += roll_count[i] * value
                else:
                    new_states[(pos_1, score_1, pos_2, score_2)] = new_states.setdefault(
                        (pos_1, score_1, pos_2, score_2), 0) + roll_count[i] * value
        self.states = new_states

    def game(self):
        last_player = 2
        while self.states:
            if last_player == 2:
                self.move_1()
                last_player = 1
            else:
                self.move_2()
                last_player = 2


def part1():
    start_pos_1, start_pos_2 = get_input()

    dirac_dice = DiracDice(start_pos_1, start_pos_2)
    print(dirac_dice.game())


def part2():
    start_pos_1, start_pos_2 = get_input()

    dirac_dice = QuantumDiracDice(start_pos_1, start_pos_2)
    dirac_dice.game()
    if dirac_dice.universes_1_win > dirac_dice.universes_2_win:
        print(dirac_dice.universes_1_win)
    else:
        print(dirac_dice.universes_2_win)


if __name__ == "__main__":
    part1()
    part2()
