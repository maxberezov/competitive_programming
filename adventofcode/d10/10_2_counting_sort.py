def count_sort(arr):
    """
    O(n+k) is time complexity. Where n is the length of the initial array and k is the maximal element in it.
    Note that is k is linearly dependant on n. Namely, the upper bound for k is 3*n+3.
    Hence, O(n+k) = O(n+3n+3) = O(4n) = O(n)
    """
    max_element = max(arr)  # O(n)
    arr.append(max_element + 3)
    max_element += 3
    arr.append(0)

    counter_arr = [0] * (max_element + 1)  # O(k)
    for elem in arr:  # O(n)

        counter_arr[elem] = 1  # We have an assumption that we can observe each element only once

    return counter_arr


def count_paths(counter_arr):  # Dynamic programming approach

    """
    O(k) is time complexity. Where k is the maximal element in the initial array.
    Note that is k is linearly dependant on n. Namely, the upper bound for k is 3*n+3.
    Hence, O(k) = O(3n+3) = O(3n) = O(n)
    """

    result = [0] * len(counter_arr)
    result[0] = 1
    for idx in range(len(counter_arr)):  # O(k)
        result[idx] += result[idx - 1] * counter_arr[idx - 1] + result[idx - 2] * counter_arr[idx - 2] + result[
            idx - 3] * counter_arr[idx - 3]
    return result[-1]


def main():
    with open('10.txt') as f:
        chargers = [int(x) for x in f.read().split('\n')]

    counted_charges = count_sort(chargers)  # O(n+k) = O(n)
    path = count_paths(counted_charges)  # O(k) = O(n)
    print('Number of paths is {}'.format(path))  # Final complexity is O(n) since k is linearly dependant on n


if __name__ == '__main__':
    main()
