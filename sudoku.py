from typing import Tuple, List


def input_sudoku() -> List[List[int]]:
    sudoku = list()
    for _ in range(9):
        row = list(map(int, input().rstrip(" ").split(" ")))
        sudoku.append(row)
    return sudoku


def print_sudoku(sudoku: List[List[int]]) -> None:
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end=" ")
        print()


# return 'this could be your solution'

def get_block_num(sudoku: List[List[int]], pos: Tuple[int, int]) -> int:
    return (pos[1] - 1) // 3 + 1 + (((pos[0] - 1) // 3)) * 3


def get_position_inside_block(sudoku: List[List[int]], pos: Tuple[int, int]) -> int:
    nb = get_block_num(sudoku, pos)
    return (pos[0] - ((nb - 1) // 3) * 3 - 1) * 3 + pos[1] - ((nb - 1) % 3) * 3


# col_decrement=((nb-1)%3)*3
# row_decrement=((nb-1)//3)*3
# pos2=(pos[0]-row_decrement,pos[1]-col_decrement)
# return (pos2[0]-1)*3+pos2[1]

def get_block(sudoku: List[List[int]], x: int) -> List[int]:
    col1 = ((x - 1) % 3) * 3
    row1 = ((x - 1) // 3) * 3
    return [sudoku[row1 + row][col1 + col] for row in range(3) for col in range(3)]


def get_row(sudoku: List[List[int]], i: int) -> List[int]:
    return sudoku[i - 1]


def get_column(sudoku: List[List[int]], x: int) -> List[int]:
    return [i[x - 1] for i in sudoku]


def find_first_unassigned_position(sudoku: List[List[int]]) -> Tuple[int, int]:
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                return (row + 1, col + 1)
    return (-1, -1)


def valid_list(lst: List[int]) -> bool:
    for i in lst:
        if i != 0 and lst.count(i) > 1:
            return False
    return True


def valid_sudoku(sudoku: List[List[int]]) -> bool:
    for i in range(1, 10):
        if valid_list(get_row(sudoku, i)):
            if valid_list(get_column(sudoku, i)):
                if valid_list(get_block(sudoku, i)):
                    continue
                else:
                    return False
            else:
                return False
        else:
            return False
    return True


def get_candidates(sudoku: List[List[int]], pos: Tuple[int, int]) -> List[int]:
    return [i for i in range(1, 10) if i not in get_row(sudoku, pos[0]) + get_column(sudoku, pos[1]) + get_block(sudoku,
                                                                                                                 get_block_num(
                                                                                                                     sudoku,
                                                                                                                     pos))]


def make_move(sudoku: List[List[int]], pos: Tuple[int, int], num: int) -> List[List[int]]:
    sudoku[pos[0] - 1][pos[1] - 1] = num
    return sudoku


def undo_move(sudoku: List[List[int]], pos: Tuple[int, int]):
    sudoku[pos[0] - 1][pos[1] - 1] = 0
    return sudoku


def sudoku_solver(sudoku: List[List[int]]) -> Tuple[bool, List[List[int]]]:
    # global d_valid_sudoku, d_get_candidates
    pos = find_first_unassigned_position(sudoku)
    if pos != (-1, -1):
        candidates = get_candidates(sudoku, pos)
        for c in candidates:
            sudoku = make_move(sudoku, pos, c)
            result = sudoku_solver(sudoku)
            if result[0]:
                # return (True, sudoku)
                return (True, result[1])
            else:
                undo_move(sudoku, pos)
        return (False, sudoku)
    v = valid_sudoku(sudoku)
    return (v, sudoku)
