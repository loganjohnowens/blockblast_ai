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
    peaces_1 = {
        'no block in slot 1': False
        'square': [[
            1, 1,
            1, 1 ], [,2 2]
        ]
        '3 by 2 horizontal': 1
        '5 long line': 1
        '4 tall line': 1
        'big corner in the botom right': 1
        'T': 1
        '2 by 3 vertical': 1
        '2 tall line': 1
        'top left corner': 1
        'big top right corner': 1
        'J pointed right': 1
        '9 by 9 square': 1
        '4 long line': 1
        'bottem left big corner': 1
        'vertical Z': 1
        'upside down T': 1
        'L pointed right': 1
        '5 tall line': 1
        'J': 1
        'Z': 1
        'S': 1
        'T pointed left': 1
    }
    peaces_2 = {
        'no block in slot 2': 1
        '4 tall line': 1
        '2 long line': 1
        'top left corner': 1
        'L pointed left': 1
        'vertical S': 1
        'corner top right': 1
        '3 long line': 1
        '2 tall line': 1
        'T pointed right': 1
        'S': 1
        'small square': 1
        '2 by 3 vertical': 1
        'big top right corner': 1
        'J': 1
        'J pointed left': 1
        'J pointed right': 1
        '9 by 9 square': 1
        '5 long line': 1
        '4 long line': 1
        '9 by 9 square': 1
        'big bottem left corner': 1
        'T': 1
        'upside down J': 1
        'upside down T': 1
        '4 long line': 1
        '9 by 9 square': 1
        'big bottem right corrner': 1
        'vertical S': 1
        '5 long line': 1
        'T pointed right': 1
        '5 tall line': 1
    }
    peaces_3 = {
        'no block in slot 3': 1
        '4 long line': 1
        '3 by 2 horizontal': 1
        'top left corner': 1
        'J pointed right': 1
        '3 long line': 1
        '2 by 3 vertical': 1
        '4 tall line': 1
        '2 tall line': 1
        'S': 1
        'Z': 1
        '9 by 9 square': 1
        '4 long line': 1
        'bottem left big corner': 1
        'vertical Z': 1
        'upside down T': 1
        'L pointed right': 1
        '5 tall line': 1
        'J': 1
        'Z': 1
        'S': 1
        'T pointed left': 1
    }

