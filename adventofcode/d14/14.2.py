from typing import Dict


def apply_bitmask(bitmask: str, input_number: int) -> str:
    output = ''
    binary_input = bin(input_number)[2:]
    if len(binary_input) < 36:
        binary_input = '0' * (36 - len(binary_input)) + binary_input

    for idx in range(len(bitmask)):
        if bitmask[idx] == '1':
            output += '1'
        elif bitmask[idx] == '0':
            output += binary_input[idx]
        else:
            output += 'X'

    return output


def save_to_memory_string(memory: Dict[int, int], input_string: str, value: int) -> None:
    if not 'X' in input_string:
        memory[int(input_string)] = value
    else:
        save_to_memory_string(memory, input_string.replace('X', '0', 1), value)
        save_to_memory_string(memory, input_string.replace('X', '1', 1), value)


def main():
    with open('14.txt') as f:
        input_data = [x for x in f.read().split('\n')]

    current_mask = ''
    memory = {}

    for data in input_data:
        if 'mask' in data:
            current_mask = data[data.index('=') + 2:]
        else:
            key = int(data[data.index('[') + 1:data.index(']')])
            value = int(data[data.index('=') + 2:])
            input_string = apply_bitmask(current_mask, key)
            save_to_memory_string(memory, input_string, value)

    print(sum(memory.values()))


if __name__ == '__main__':
    main()
