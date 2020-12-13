from typing import List, Tuple


def rotate_waypoint(waypoint: List[int], direction: str, angle: int) -> List[int]:
    """
    This function rotates waypoint list according to the given angle

    Complexity: O(1)
    """
    shift = angle // 90

    if direction == 'R':
        return [waypoint[idx - shift] for idx in range(len(waypoint))]
    else:
        return [waypoint[idx - 4 + shift] for idx in range(len(waypoint))]


def get_idx(directions: List[str]) -> Tuple[int, int, int, int]:
    """
    return idx for each rotation_direction from dir list in this order 'NESW'
    Complexity: O(1)
    """
    return directions.index('N'), directions.index('E'), directions.index('S'), directions.index('W')


def perform_action(action: Tuple[str, int], waypoint: List[int], counter: List[int], directions: List[str]) -> Tuple[List[int], List[int]]:
    """
    Updates waypoint list and counter list based on the action
    Complexity: O(1)
    """
    direction = action[0]
    value = action[1]

    if direction in directions:
        waypoint[directions.index(direction)] += value
    elif direction == 'F':
        north_idx, east_idx, south_idx, west_idx = get_idx(directions)
        north_shift = waypoint[north_idx] - waypoint[south_idx]
        east_shift = waypoint[east_idx] - waypoint[west_idx]
        counter[north_idx] += north_shift * value
        counter[east_idx] += east_shift * value
    elif direction == 'L':
        waypoint = rotate_waypoint(waypoint, 'L', value)
    else:
        waypoint = rotate_waypoint(waypoint, 'R', value)

    return waypoint, counter


def main():
    with open('12.txt') as f:
        array = [(x[0], int(x[1:])) for x in f.read().split('\n')]

    counter = [0, 0, 0, 0]
    waypoint = [10, 0, 0, 1]  # east south west north
    directions = ['E', 'S', 'W', 'N']
    for element in array:  # O(n)
        waypoint, counter = perform_action(element, waypoint, counter, directions)  # O(1)

    north_idx, east_idx, south_idx, west_idx = get_idx(directions)
    print(abs(counter[north_idx] - counter[south_idx]) + abs(counter[east_idx] - counter[west_idx]))


if __name__ == '__main__':
    main()
