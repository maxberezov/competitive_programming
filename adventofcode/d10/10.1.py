def count_difference(arr):
    """
    Time complexity of this function is O(n)
    """
    differences = [1, 3]
    counts = [0, 0]

    for idx in range(len(arr) - 1):  # we visit each element of our list, O(n) is complexity
        diff = arr[idx + 1] - arr[idx]
        if diff in differences:  # O(1)
            counts[differences.index(diff)] += 1  # O(1)

    return counts[0] * counts[1]


def main():
    with open('10.txt') as f:
        chargers = [int(x) for x in f.read().split('\n')]

    chargers.append(0)
    chargers = sorted(chargers)  # Complexity is O(n*log(n))
    chargers.append(chargers[-1] + 3)
    print('Difference is {}'.format(count_difference(chargers)))  # Final complexity is O(n*log(n))


if __name__ == '__main__':
    main()