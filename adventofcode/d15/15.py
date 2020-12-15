from typing import Dict, Tuple, Union


def update_spoken_numbers(spoken_numbers: Dict[int, Tuple[int, Union[None, int], int]], number: int, idx: int) -> None:
    """
    This function updates the list of already spoken digits.
    Digit is a key, values are its counter, and indices of string_end two entries (maybe None if it has one entry).
    """

    if number in spoken_numbers.keys():  # O(1)
        value, idx_prev, idx_last = spoken_numbers[number]
        value += 1
        idx_prev = idx_last
        idx_last = idx
        spoken_numbers[number] = (value, idx_prev, idx_last)
    else:
        spoken_numbers[number] = (1, None, idx)


def update_current_number(spoken_numbers: Dict[int, Tuple[int, Union[None, int], int]], last_said_number: int,
                          curr_idx: int) -> int:
    """
    Total complexity is O(1)
    """

    if spoken_numbers[last_said_number][0] == 1:
        update_spoken_numbers(spoken_numbers, 0, curr_idx)
        last_said_number = 0

    else:
        value, idx_prev, idx_last = spoken_numbers[last_said_number]
        update_spoken_numbers(spoken_numbers, idx_last - idx_prev, curr_idx)
        last_said_number = idx_last - idx_prev

    return last_said_number


def iterative_update(spoken_numbers: Dict[int, Tuple[int, Union[None, int], int]], curr_idx: int, last_said_number: int,
                     iterations: int) -> int:
    while curr_idx != iterations:
        last_said_number = update_current_number(spoken_numbers, last_said_number, curr_idx)
        curr_idx += 1
    return last_said_number


def main():
    with open('15.txt') as f:
        input_data = [int(x) for x in f.read().split(',')]

    spoken_numbers = {}

    for idx in range(len(input_data)):
        update_spoken_numbers(spoken_numbers, input_data[idx], idx)

    last_said_number = input_data[-1]
    curr_idx = len(input_data)
    iterations = 30000000
    last_said_number = iterative_update(spoken_numbers, curr_idx, last_said_number, iterations)
    print(last_said_number)


if __name__ == '__main__':
    main()
