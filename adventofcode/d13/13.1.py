def main():
    with open('13.txt') as f:
        input_data = [x for x in f.read().split('\n')]
        timestamp = int(input_data[0])
        buses = [int(element) for element in input_data[1].split(',') if element != 'x']

    # Total complexity is O(n)
    remaining_times = [bus - timestamp % bus for bus in buses]  # O(n)
    min_element = min(remaining_times)  # O(n)
    bus = buses[remaining_times.index(min_element)]  # O(n)

    print(min_element * bus)


if __name__ == '__main__':
    main()
