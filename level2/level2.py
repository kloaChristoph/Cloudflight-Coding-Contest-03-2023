
def load_file(filename: str = "level1/level1_1.in") -> list:
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]


def write_to_file(data: list, filename: str = "level1/level1_1.out") -> None:
    with open(filename, "w") as file:
        for line in data:
            file.write(line + "\n")


def tournament(data: list) -> list:
    winner = []
    for tourn in data[1:]:
        if win := check_tournament_winners(tourn):
            winner.append(win)
    return winner


if __name__ == '__main__':
    for i in range(1, 5):
        comp = tournament(load_file(f"level2/level2_{i}.in"))
        write_to_file(comp, f"level2/level2_{i}.out")
