def read_input_test_case(file_path: str) -> dict:
    line_number = 0
    array_size = 0
    queries = []
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
        while line_number < len(lines):
            if line_number == 0:
                array_size = int(lines[line_number].split(' ')[0])
            else:
                queries.append([int(value) for value in lines[line_number].split(' ')])
            line_number += 1
    return {
        "n": int(array_size),
        "queries": queries,
    }


def array_manipulation_bf(n: int, queries: list[list[int]]) -> int:
    # print(f"Input: n = {n}; queries = {queries}")
    max_value = 0
    a = [0] * n
    row = 0
    while row < len(queries):
        start = queries[row][0] - 1
        end = queries[row][1] - 1
        value = queries[row][2]
        index = start
        while index <= end:
            if a[index] == 0:
                a[index] = value
            else:
                a[index] += value
            if a[index] > max_value:
                max_value = a[index]
            # if index == end:
            #     print(f"Index: {index}; End: {end}; Array: {a}")
            index += 1
        row += 1
    # print(f"Max Value: {max_value}; Final Array: {a}")
    return max_value


def array_manipulation(n: int, queries: list[list[int]]) -> int:
    # Solution by using Sum Prefix Array
    a = [0] * (n + 1)
    for n in range(len(queries)):
        a[queries[n][0] - 1] += queries[n][2]
        a[queries[n][1] + 1] -= queries[n][2]
    maximum = 0
    total = 0
    for n in range(len(a)):
        total += a[n]
        maximum = max(maximum, total)
    return maximum
