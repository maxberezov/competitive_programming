from itertools import product
from typing import List, Tuple

FREE = 'L'
OCCUPIED = '#'


def count_adjacent_seats(seats: List[str], i: int, j: int) -> Tuple[int, int]:
    """
    Let m be the number of columns, k - number of rows. m*k = n
    Total complexity of this function is O(max(m,k)). The worst case is O(n).
    """

    occupied = 0
    free = 0

    adj_idx = list(product([-1, 0, 1], repeat=2))
    adj_idx.remove((0, 0))

    for idx in adj_idx:  # O(1)
        for mult_term in range(1, max(len(seats), len(seats[0]))):  # O(max(m,k))
            if len(seats) > i + idx[0] * mult_term >= 0 and len(seats[j]) > j + idx[1] * mult_term >= 0:
                curr_neighbour = seats[i + idx[0] * mult_term][j + idx[1] * mult_term]
                if curr_neighbour == OCCUPIED:
                    occupied += 1
                    break
                elif curr_neighbour == FREE:
                    free += 1
                    break
    return occupied, free


def apply_single_iteration(lines: List[str]) -> Tuple[List[str], bool]:
    """
    Let m be the number of columns, k - number of rows. m*k = n
    Total complexity of this function is O(n)*O(max(m,k)). The worst case is O(n^2).

    """

    updated_lines = ['.' * len(lines[0]) for _ in range(len(lines))]  # O(m)
    any_modifications = False
    for i, line in enumerate(lines):  # O(m)
        for j, seat in enumerate(line):  # O(k)
            occupied, free = count_adjacent_seats(lines, i, j)  # O(max(m,k))
            if occupied == 0 and lines[i][j] == FREE:
                updated_lines[i] = updated_lines[i][:j] + OCCUPIED + updated_lines[i][j + 1:]
                any_modifications = True
            elif occupied >= 5 and lines[i][j] == OCCUPIED:
                updated_lines[i] = updated_lines[i][:j] + FREE + updated_lines[i][j + 1:]
                any_modifications = True
            else:
                updated_lines[i] = updated_lines[i][:j] + lines[i][j] + updated_lines[i][j + 1:]
    return updated_lines, any_modifications


def count_occupied_seats(seats: List[str]) -> int:
    """
    Total complexity is O(n)
    """
    counter = 0
    for line in seats:
        for seat in line:
            if seat == OCCUPIED:
                counter += 1
    return counter


def main():
    with open('11.txt') as f:
        lines = f.read().split('\n')

    flag = True
    while flag:
        lines, modifications = apply_single_iteration(lines)  # O(n)*O(max(m,k))
        flag = modifications

    print(count_occupied_seats(lines))


if __name__ == '__main__':
    main()
