def apply_bitmask(bitmask: str, input_value: int) -> int:
    output_string = ''
    binary_input = bin(input_value)[2:]

    if len(binary_input) < 36:
        binary_input = '0' * (36 - len(binary_input)) + binary_input

    for idx in range(len(bitmask)):
        if bitmask[idx] == 'X':
            output_string += binary_input[idx]
        else:
            output_string += bitmask[idx]

    decimal_value = int(output_string, 2)
    return decimal_value


def main():
    with open('14.txt') as f:
        input_data = [x for x in f.read().split('\n')]

    memory = {}
    current_mask = ''

    for data in input_data:
        if 'mask' in data:
            current_mask = data[data.index('=') + 2:]
        else:
            key = int(data[data.index('[') + 1:data.index(']')])
            value = int(data[data.index('=') + 2:])
            memory[key] = apply_bitmask(current_mask, value)

    print(sum(memory.values()))


if __name__ == '__main__':
    main()
