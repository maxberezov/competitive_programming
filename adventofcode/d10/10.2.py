def count_paths(arr, n):  # Dynamic programming approach
    """
    Time complexity of this function is O(n)
    """
    result = [0] * n
    result[0] = 1
    differences = [1, 2, 3]

    for i in range(1, n):  # iterate over all elements in the list, complexity is O(n)
        for k in range(1, min(i + 1, 4)):  # just 3 iterations maximum; constant complexity O(1)
            if arr[i] - arr[i - k] in differences:  # O(1)
                result[i] += result[i - k]

    return result[-1]


def main():
    with open('10.txt') as f:
        chargers = [int(x) for x in f.read().split('\n')]

    chargers.append(0)
    chargers = sorted(chargers)  # Complexity is O(n*log(n))
    chargers.append(chargers[-1] + 3)

    print('Number of paths is {}'.format(count_paths(chargers, len(chargers))))  # O(n)
    # Final complexity is O(n*log(n)) since n*log(n) > n


if __name__ == '__main__':
    main()
