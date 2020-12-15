from typing import Set


def take_max_possible_from_set(options: Set, current_sum: int) -> int:
    """
    Complexity of this function is O(1). It does 9 iterations maximum
    """

    digits = list(options)

    while len(digits) > 0:  # O(1)
        max_digit = max(digits)
        if max_digit > current_sum:
            digits.remove(max_digit)
        else:
            return max_digit
    return -1


t = int(input())

for i in range(t):

    n = int(input())

    possible_digits = set([x for x in range(1, 10)])
    new_number = []
    flag = True

    while n != 0:
        curr_digit = take_max_possible_from_set(possible_digits, n)
        if curr_digit == -1:
            print('-1')
            flag = False
            break
        else:
            n -= curr_digit
            possible_digits.remove(curr_digit)
            new_number.append(curr_digit)
    if flag:
        print(''.join([str(i) for i in new_number[::-1]]))
