from typing import List, Dict, Tuple, Set


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


def add_to_dict(d: Dict[str, Set[int]], value: int, key: str):
    if key in d.keys():
        d[key].add(value)
    else:
        d[key] = set()
        d[key].add(value)


def find_idx_fields(constraints: Dict[str, Tuple[List[int], List[int]]], valid_tickets: List[List[int]]) -> Dict[
    str, Set[int]]:
    """
    Total complexity of this function is O(n*(k^2))
    """

    field_corresponding = {}
    for constraint in constraints.keys():  # O(k)
        for idx in range(len(valid_tickets[0])):  # O(k)

            counter = 0
            for ticket in valid_tickets:  # O(n)
                if check_constrain(constraints, constraint, ticket[idx]):
                    counter += 1

            if counter == len(valid_tickets):
                add_to_dict(field_corresponding, idx, constraint)

    return field_corresponding


def find_valid_tickets(constraints: Dict[str, Tuple[List[int], List[int]]], tickets: List[List[int]]) -> List[
    List[int]]:
    """
    Complexity is O(n*k^2 + n^2)

    """

    invalid_tickets = []

    for idx, ticket in enumerate(tickets):  # O(n)
        for field in ticket:  # O(k)
            if not check_all_constraints(constraints, field):  # O(k)
                invalid_tickets.append(ticket)
                break

    valid_tickets = [x for x in tickets if x not in invalid_tickets]  # O(n^2)
    return valid_tickets


def find_field_idx_bijection(field_corresponding: Dict[str, Set[int]]) -> Dict[str, int]:
    # Complexity is O(k^2)
    bijection = {}
    allocated = set()

    while len(bijection.keys()) != len(field_corresponding.keys()):  # O(k)
        for k, v in field_corresponding.items():  # O(k)
            if len(v - allocated) == 1:  # Amortized
                idx = v.pop()
                v.add(idx)
                allocated.add(idx)
                bijection[k] = idx
    return bijection


def main():
    with open('16.txt') as f:
        input_data = [x for x in f.read().split('\n')]
        separator_idx = [idx for idx in range(len(input_data)) if len(input_data[idx]) == 0]

    # Let n - the number of tickets, k - the number of  fields
    constraints = parse_bounds(input_data[:separator_idx[0]])  # O(k)
    tickets = parse_tickets(input_data[separator_idx[1] + 2:])  # O(n)
    my_ticket = input_data[separator_idx[0] + 2:separator_idx[1] + 1][0].split(',')  # O(k)
    my_ticket = [int(x) for x in my_ticket]  # O(k)
    valid_tickets = find_valid_tickets(constraints, tickets)  # O(n*k^2 + n^2)
    correspondence = find_idx_fields(constraints, valid_tickets)  # O(n*(k^2))
    bijection = find_field_idx_bijection(correspondence)  # O(k^2)

    answer = 1

    for k, v in bijection.items():  # O(k)
        if 'departure' in k:
            answer *= my_ticket[v]

    print(answer)

    # Total complexity of this code is O(n*k^2 + n^2)


if __name__ == '__main__':
    main()
