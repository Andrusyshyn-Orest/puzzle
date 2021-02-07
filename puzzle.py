"""
GitHub Repository: https://github.com/Andrusyshyn-Orest/puzzle

This module checks if board is ready for puzzle game.

>>> check_row_uniqueness([\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"\
])
True

>>> check_column_uniqueness([\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"\
])
False

>>> check_block_uniqueness([\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"\
])
True

>>> validate_board([\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"\
])
False
"""
# def check_not_colored(board: list) -> bool:
#     """
#     """
#     global NUMBER
#     white_board = ['*'*NUMBER]*NUMBER

def check_row_uniqueness(board: list) -> bool:
    """
    Return True if each row has no repeated digits.
    Return False otherwise.

    >>> check_row_uniqueness([\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"\
])
    True

    >>> check_row_uniqueness([\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 " 5   9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"\
])
    False
    """

    global NUMBER
    for row in board:
        count = 0
        row_set = set()
        for char in row:
            if char.isdigit():
                if int(char) in range(1, NUMBER + 1):
                    count += 1
                    row_set.add(char)
        if len(row_set) != count:
            return False
    return True


def check_column_uniqueness(board: list) -> bool:
    """
    Return True if each column has no repeated digits.
    Return False otherwise.

    >>> check_column_uniqueness([\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"\
])
    False

    >>> check_column_uniqueness([\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   2  **",\
 "  8  2***",\
 "  2  ****"\
])
    True
    """

    global NUMBER
    columns = []
    for col_ind in range(NUMBER):
        column = ''
        for row in board:
            column += row[col_ind]
        columns.append(column)
    return check_row_uniqueness(columns)


def check_block_uniqueness(board: list) -> bool:
    """
    Return True if each colored block has no repeated digits.
    Return False otherwise.

    >>> check_block_uniqueness([\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"\
])
    True

    >>> check_block_uniqueness([\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  6***",\
 "  2  ****"\
])
    False
    """

    global NUMBER
    size = (NUMBER // 2) + 1
    columns = []
    for col_ind in range(NUMBER):
        column = ''
        for row in board:
            column += row[col_ind]
        columns.append(column)

    for ind in range(size):
        col = columns[ind][NUMBER - size - ind: NUMBER - ind]
        row = board[-(ind + 1)][ind + 1: size + ind]
        block_str = ''.join(col.split()) + ''.join(row.split())
        block_set = set(block_str)
        if len(block_set) != len(block_str):
            return False
    return True



def validate_board(board: list) -> bool:
    """
    Return True if board meets the rules.
    Return False otherwise.

    >>> validate_board([\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"\
])
    False

    >>> validate_board([\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   9  **",\
 "  8  2***",\
 "  2  ****"\
])
    True

    >>> validate_board([\
 "**** ****",\
 "***  ****",\
 "**   ****",\
 "*    ****",\
 "         ",\
 "        *",\
 "       **",\
 "      ***",\
 "     ****"\
])
    True
    """

    if not check_row_uniqueness(board):
        return False
    if not check_column_uniqueness(board):
        return False
    if not check_block_uniqueness(board):
        return False
    return True


if __name__ == "__main__":
    import doctest
    NUMBER = 9
    print(doctest.testmod())
else:
    NUMBER = 9
