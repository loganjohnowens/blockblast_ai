from screen_interpeter import exe_interpreter
import time
peaces_we_have = exe_interpreter()


def AI():
    global slot_1
    global slot_2
    global slot_3
    global game_state
    get_pieces()


def get_pieces():
    global slot_1
    global slot_2
    global slot_3
    global peaces
    peaces = {
        'no block in slot 1': False,
        'no block in slot 2': False,
        'no block in slot 3': False,
        'square': [[
            1, 1,
            1, 1], [2, 2]
        ],
        '3 by 2 horizontal':
            [[1, 1, 1,
              1, 1, 1], [3, 2]],
        '5 long line':
            [[1, 1, 1, 1, 1,], [5, 1]],
        '4 tall line':
            [[1,
              1,
              1,
              1, ], [1, 4]],
        'big corner in the botom right':
            [[0, 0, 1,
              0, 0, 1,
              1, 1, 1], [3, 3]],
        'T':
            [[1, 1, 1,
              0, 1, 0,
             0, 1, 0], [3, 3]],
        '2 by 3 vertical':
            [[1, 1,
              1, 1,
              1, 1], [2, 3]],
        '2 tall line':
            [[1,
              1], [1, 2]],
        'top left corner':
            [[1, 1,
              1, 0], [2, 2]],
        'big top right corner':
            [[1, 1, 1,
              1, 0, 0,
              1, 0, 0], [3, 3]],
        'J pointed right':
            [[1, 0, 0,
              1, 1, 1,], [3, 2]],
        '9 by 9 square':
            [[1, 1, 1,
              1, 1, 1,
              1, 1, 1], [3, 3]],
        '4 long line':
            [[1, 1, 1, 1], [4, 1]],
        'bottem left big corner':
            [[1, 0, 0,
              1, 0, 0,
              1, 0, 0], [3, 3]],
        'vertical Z':
            [[0, 1,
              1, 1,
              1, 0], [2, 3]],
        'upside down T':
            [[0, 1, 0,
              0, 1, 0,
              1, 1, 1], [3, 3]],
        'L pointed right':
            [[1, 1, 1,
              1, 0, 0,], [3, 2]],
        '5 tall line':
            [[1,
             1,
             1,
             1,
             1], [1, 5]],
        'J':
            [[0, 1,
              0, 1,
              1, 1], [2, 3]],
        'Z':
            [[1, 1, 0,
              0, 1, 1], [3, 2]],
        'S':
            [[0, 1, 1,
              1, 1, 0], [3, 2]],
        'T pointed left':
            [[0, 0, 1,
              1, 1, 1,
              0, 0, 1], [3, 3]],
        '3 long line':
            [[1, 1, 1], [3, 1]]
    }


def test():
    get_pieces()
    print(f'the grid for slot 1 is ({peaces[peaces_we_have[0]]})')
    print(f'the grid for slot 2 is ({peaces[peaces_we_have[1]]})')
    print(f'the grid for slot 3 is ({peaces[peaces_we_have[2]]})')
    board_formate_changer()
    display_a_board(board)
    valid_places()


def display_a_board(display):
    for i in [0, 8, 16, 24, 32, 40, 48]:
        print(display[i], display[i + 1], display[i + 2], display[i + 3],
              display[i + 4], display[i + 5], display[i + 6], display[i + 7])


def board_formate_changer():
    global board
    board = []
    for i in peaces_we_have[3]:
        if i == 'b':
            board.append(0)
        if i == 'f':
            board.append(1)


def get_cordents(cords, size):
    half = cords[1] * size[1]
    other_half = size[0] - cords[0]
    last_bit = half - other_half
    return last_bit - 1


def valid_places():
    global possible_boards
    possible_boards = []
    current_peace = peaces[peaces_we_have[2]]
    cords = [1, 1]
    base_number = [0, 0]
    board_check = []
    cords_check = []
    while True:
        cords[0] = base_number[0] + 1
        cords[1] = base_number[1] + 1
        while True:
            print(f'begin {cords} {cords_check}')
            board_check.append(board[get_cordents(cords, [8, 8])])
            cords_check.append(cords)
            print(f' end {cords, cords_check}')
            cords[0] += 1
            if cords[0] > current_peace[1][0] + base_number[0]:
                cords[0] = base_number[0] + 1
                cords[1] += 1
            if cords[1] > current_peace[1][1] + base_number[1]:
                break
        can_work = check_if_valid(board_check, current_peace[0])
        make_new_game_state(can_work, current_peace, cords_check)
        base_number[0] += 1
        board_check = []
        cords_check = []
        if base_number[0] + current_peace[1][0] > 8:
            base_number[0] = 0
            base_number[1] += 1
        if base_number[1] + current_peace[1][1] > 8:
            break


def check_if_valid(board, peace):
    possible = True
    times = -1
    for i in board:
        if i == peace[times] == 1:
            possible = False
        times += 1
    return possible


def make_new_game_state(can_this_work, peace, locatoins):
    global possible_boards
    if can_this_work:
        possible_boards.append([board, [0]])
        for i in range(0, len(peace[0])):
            if peace[0][i] == 1:
                possible_boards[0][0][get_cordents(locatoins[i], [8, 8])] = peace[0][i]
                print(locatoins[i])
        print('--------------------------------------------------------------------------')
        display_a_board(possible_boards[0][0])


def main():
    get_pieces()
    board_formate_changer()
    valid_places()


test()
