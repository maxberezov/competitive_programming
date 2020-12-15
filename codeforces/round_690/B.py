t = int(input())

for i in range(t):
    s_len = int(input())
    s = input()

    pattern = '2020'
    string_start = s[:4]
    string_end = s[-4:]
    possible_strings = set()

    for idx in range(len(pattern)+1):
        possible_strings.add(string_start[:idx] + string_end[idx:])

    if pattern in possible_strings:
        print('YES')
    else:
        print('NO')

