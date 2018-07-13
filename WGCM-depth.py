MAN = 0
WOLF = 1
GOAT = 2
CABBAGE = 3
SEARCH_MAX = 20
left_side = [[]]
right_side = [[]]


def print_state(state):
    out = ''
    for index, state in enumerate(state):
        if state == 1:
            if index == 0:
                out += ' 男 '
            elif index == 1:
                out += ' 狼 '
            elif index == 2:
                out += ' 山羊 '
            elif index == 3:
                out += ' キャベツ '

    return '[%s]' % out


def print_ans():
    pass


def check_state():
    pass


def search():
    pass


def main():
    pass


if __name__ == '__main__':
    main()
