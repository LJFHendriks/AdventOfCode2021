def get_input(filename="input.txt"):
    with open(filename, "r") as file:
        line = file.read()
    return line


Hex2Bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}


class Packet:
    def __init__(self, binary, start):
        position = start
        self.start = start
        self.packet_version = int(binary[position:position + 3], 2)
        position += 3

        self.packet_type = int(binary[position:position + 3], 2)
        position += 3

        self.sub_packets = list()
        if self.packet_type == 4:
            value = ""
            while binary[position] != "0":
                value += binary[position + 1: position + 5]
                position += 5
            value += binary[position + 1: position + 5]
            position += 5
            self.value = int(value, 2)
        else:
            self.length_type = int(binary[position], 2)
            position += 1
            if self.length_type == 0:
                total_length = int(binary[position: position + 15], 2)
                position += 15
                start_position = position
                while position < start_position + total_length:
                    new_packet = Packet(binary, position)
                    self.sub_packets.append(new_packet)
                    position += new_packet.end - new_packet.start
            elif self.length_type == 1:
                number_of_packets = int(binary[position: position + 11], 2)
                position += 11
                for i in range(number_of_packets):
                    new_packet = Packet(binary, position)
                    self.sub_packets.append(new_packet)
                    position += new_packet.end - new_packet.start
        self.end = position

    def sum_version_numbers(self):
        total = 0
        for packet in self.sub_packets:
            total += packet.sum_version_numbers()
        return total + self.packet_version

    def eval(self):
        if self.packet_type == 4:
            return self.value
        elif self.packet_type == 0:
            return sum([packet.eval() for packet in self.sub_packets])
        elif self.packet_type == 1:
            total = 1
            for packet in self.sub_packets:
                total *= packet.eval()
            return total
        elif self.packet_type == 2:
            return min([packet.eval() for packet in self.sub_packets])
        elif self.packet_type == 3:
            return max([packet.eval() for packet in self.sub_packets])
        elif self.packet_type == 5:
            return 1 if self.sub_packets[0].eval() > self.sub_packets[1].eval() else 0
        elif self.packet_type == 6:
            return 1 if self.sub_packets[0].eval() < self.sub_packets[1].eval() else 0
        elif self.packet_type == 7:
            return 1 if self.sub_packets[0].eval() == self.sub_packets[1].eval() else 0


def part1():
    line = get_input()
    binary = ""
    for char in line:
        binary += Hex2Bin[char]

    packet = Packet(binary, 0)
    print(packet.sum_version_numbers())


def part2():
    line = get_input()
    binary = ""
    for char in line:
        binary += Hex2Bin[char]

    packet = Packet(binary, 0)
    print(packet.eval())


if __name__ == "__main__":
    part1()
    part2()
