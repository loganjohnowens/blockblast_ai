from screen_interpeter import exe_interpreter

exe_interpreter()


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
        '2 by 3 vertical': 1
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
              1, 1, 1], [9, 9]],
        '4 long line': 1
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
              0, 0, 1], [3, 3]]
    }
