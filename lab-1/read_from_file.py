from Helicopter import Helicopter


def read_from_file(filename):
    with open(filename) as f:
        list_of_helicopters = []
        for line in f:
            line = line.strip("\n").split(",")
            list_of_helicopters.append(Helicopter(line[0], line[1], line[2]))
    return list_of_helicopters
