from pprint import pprint

col, row = map(int, input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))
pprint(matrix, indent=2)


def countMines(i, k):
    if matrix[i][k] == '*':
        return '*'

    count = 0
    for r in range(i - 1, i + 2):
        for c in range(k - 1, k + 2):
            if r < 0 or c < 0 or r >= row or c >= col:
                continue
            if matrix[r][c] == '*':
                count += 1
    return count


for i in range(row):
    for k in range(col):
        print(countMines(i, k), end='')
    print()