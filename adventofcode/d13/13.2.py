from typing import List, Tuple


def compute_multiplication_list(buses: List[int]) -> Tuple[int, List[int]]:
    """
    Chinese remainder theorem
    Time complexity: O(n)
    """

    multiplication = 1
    multiplication_list = []

    for bus in buses:  # O(n)
        if bus != 0:
            multiplication *= bus

    for bus in buses:  # O(n)
        if bus != 0:
            multiplication_list.append(multiplication // bus)

    return multiplication, multiplication_list


def compute_coefficients(multiplication_list: List[int], not_empty_buses: List[int]) -> List[int]:
    """
    Computes coefficients as a part of Chinese remainder theorem
    We have an assumption that coefficients are less than 1000, otherwise change the upper bound
    Complexity is O(n)
    """
    coefficients = []
    upper_bound = 1000
    for idx in range(len(multiplication_list)):  # O(n)
        for i in range(upper_bound):  # Could be solved in analytical way but I'm lazy.
            if (multiplication_list[idx] * i) % not_empty_buses[idx] == 1:
                coefficients.append(i)
                break
    return coefficients


def compute_answer(coefficients: List[int], multiplication_list: List[int], buses: List[int],
                   not_empty_buses: List[int],
                   multiplication: int) -> int:
    """
    Computes final answer as a part of Chinese remainder theorem
    Time complexity is O(n)

    """
    answer = 0
    for idx in range(len(multiplication_list)):  # O(n)
        tmp_reminder = not_empty_buses[idx] - buses.index(not_empty_buses[idx])
        answer += multiplication_list[idx] * coefficients[idx] * tmp_reminder
    return answer % multiplication


def main():
    with open('13.txt') as f:
        input_data = [x for x in f.read().split('\n')]
        buses = [int(element) if element != 'x' else 0 for element in input_data[1].split(',')]
        not_empty_buses = [int(element) for element in input_data[1].split(',') if element != 'x']

    # Total complexity is O(n)
    multiplication, multiplication_list = compute_multiplication_list(buses)  # O(n)
    coefficients = compute_coefficients(multiplication_list, not_empty_buses)  # O(n)
    answer = compute_answer(coefficients, multiplication_list, buses, not_empty_buses, multiplication)  # O(n)
    print(answer)


if __name__ == '__main__':
    main()
