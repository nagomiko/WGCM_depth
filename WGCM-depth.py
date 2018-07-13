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


def print_ans(t):
    for i in range(t):
        print('%d : %s %s' % (i, print_state(left_side[t]), print_state(right_side[t])))


def check_state(t, state, past_state):
    pass


def search(t, src_side, dest_side):
    pass


def main():
    global left_side, right_side
    left_side = [[-1 for i in range(4)] for j in range(SEARCH_MAX)]
    right_side = [[-1 for i in range(4)] for j in range(SEARCH_MAX)]
    left_side[0][:] = [1, 1, 1, 1]
    right_side[0][:] = [0, 0, 0, 0]
    search(0, left_side, right_side)


if __name__ == '__main__':
    main()
