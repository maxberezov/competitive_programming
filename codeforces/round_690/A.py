t = int(input())

for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().split(' ')]

    transformed_array = []
    for idx in range(len(arr) // 2):
        transformed_array.append(arr[idx])
        transformed_array.append(arr[-1 - idx])

    if len(arr) % 2 != 0:
        transformed_array.append(arr[len(arr) // 2])

    print(*transformed_array)
