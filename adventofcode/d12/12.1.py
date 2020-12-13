from typing import List, Tuple


def rotate_current_direction(current_direction: str, rotation_direction: str, angle: int, directions: List[str]) -> str:
    """
    This function rotates current direction according to the given angle

    Complexity: O(1)
    """
    shift = angle // 90

    if rotation_direction == 'R':
        return directions[directions.index(current_direction)-4+shift]
    else:
        return directions[directions.index(current_direction)-shift]


def get_idx(directions: List[str]) -> Tuple[int, int, int, int]:
    """
    return idx for each rotation_direction from dir list in this order 'N-E-S-W'
    Complexity: O(1)
    """
    return directions.index('N'), directions.index('E'), directions.index('S'), directions.index('W')


def perform_action(action: Tuple[str, int], current_direction: str, counter: List[int], directions: List[str]) -> Tuple[str, List[int]]:
    """
    Updates current rotation_direction and counter list based on the action
    Complexity: O(1)
    """
    direction = action[0]
    value = action[1]

    if direction in directions:
        counter[directions.index(direction)] += value
    elif direction == 'F':
        counter[directions.index(current_direction)] += value
    elif direction == 'L':
        current_direction = rotate_current_direction(current_direction, 'L', value, directions)
    else:
        current_direction = rotate_current_direction(current_direction, 'R', value,directions)

    return current_direction, counter


def main():
    with open('12.txt') as f:
        array = [(x[0], int(x[1:])) for x in f.read().split('\n')]

    counter = [0, 0, 0, 0]
    directions = ['E', 'S', 'W', 'N']
    current_direction = 'E'

    for element in array:  # O(n)
        current_direction, counter = perform_action(element, current_direction, counter, directions)  # O(1)

    north_idx, east_idx, south_idx, west_idx = get_idx(directions)
    print(abs(counter[north_idx] - counter[south_idx]) + abs(counter[east_idx] - counter[west_idx]))


if __name__ == '__main__':
    main()
