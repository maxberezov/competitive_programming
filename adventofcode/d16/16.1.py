from typing import List, Dict, Tuple


def parse_bounds(input_data: List[str]) -> Dict[str, Tuple[List[int], List[int]]]:
    constraints = {}
    for data in input_data:
        field = data[:data.index(':')]
        first_bound = [int(x) for x in data[data.index(':') + 2:data.index('or ') - 1].split('-')]
        second_bound = [int(x) for x in data[data.index('or ') + 3:].split('-')]
        constraints[field] = first_bound, second_bound
    return constraints


def parse_tickets(input_data: List[str]) -> List[List[int]]:
    tickets = []
    for data in input_data:
        tickets.append([int(x) for x in data.split(',')])
    return tickets


def check_constrain(constraints: Dict[str, Tuple[List[int], List[int]]], constraint: str, value: int) -> bool:
    if constraints[constraint][0][0] <= value <= constraints[constraint][0][1] or constraints[constraint][1][
        0] <= value <= constraints[constraint][1][1]:
        return True
    else:
        return False


def check_all_constraints(constraints: Dict[str, Tuple[List[int], List[int]]], value: int) -> bool:
    for constraint in constraints.keys():  # O(k)
        if check_constrain(constraints, constraint, value):
            return True
    return False


def main():
    with open('16.txt') as f:
        input_data = [x for x in f.read().split('\n')]
        separator_idx = [idx for idx in range(len(input_data)) if len(input_data[idx]) == 0]

    # Let n - the number of tickets, k - the number of  fields
    constraints = parse_bounds(input_data[:separator_idx[0]])  # O(k)
    tickets = parse_tickets(input_data[separator_idx[1] + 2:])  # O(n)

    counter = 0
    # Total complexity of this loop is O(n*(k^2))
    for ticket in tickets:  # O(n)
        for field in ticket:  # O(k)
            if not check_all_constraints(constraints, field):  # O(k)
                counter += field

    print(counter)

    # Total complexity is O(n*(k^2))


if __name__ == '__main__':
    main()
