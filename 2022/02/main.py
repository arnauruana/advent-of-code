import sys


ROCK = 1
PAPER = 2
SCISSORS = 3

SHAPE = {
    'A': ROCK,
    'X': ROCK,
    'B': PAPER,
    'Y': PAPER,
    'C': SCISSORS,
    'Z': SCISSORS,
}

LOSE = 0
DRAW = 3
WIN = 6

RESULT = {
    'X': LOSE,
    'Y': DRAW,
    'Z': WIN,
}


def read_input():
    lines = []
    while (True):
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break
    return lines


def translate(strategy, shape=True):
    enemy_letter, ally_letter = strategy

    enemy_shape = SHAPE[enemy_letter]
    ally_shape = SHAPE[ally_letter] if shape else RESULT[ally_letter]

    strategy = (enemy_shape, ally_shape)
    return strategy


def outcome_result(enemy, ally):
    if (ally == enemy):
        return DRAW
    if (ally - enemy%3 == 1):
        return WIN
    return LOSE


def outcome_shape(shape, result):
    if result == LOSE:
        return (shape-2) % 3 + 1
    if result == DRAW:
        return shape
    return shape%3 + 1


def score(strategy):
    enemy_shape, ally_shape = strategy

    shape_score = ally_shape
    result_score = outcome_result(enemy_shape, ally_shape)

    return shape_score + result_score


def score2(strategy):
    enemy_shape, ally_result = strategy

    shape_score = outcome_shape(enemy_shape, ally_result)
    result_score = ally_result

    return shape_score + result_score


def main(_):
    strats = read_input()
    strats = [tuple(strat.split()) for strat in strats]

    scores = [score(translate(strat, shape=True)) for strat in strats]
    print(sum(scores))

    scores = [score2(translate(strat, shape=False)) for strat in strats]
    print(sum(scores))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
