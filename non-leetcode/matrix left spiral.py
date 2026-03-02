n = int(input())
m = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
while matrix:
    print(*matrix.pop(0), end=" ")
    for row in matrix:
        if row:
            print(row.pop(), end=" ")
    if matrix:
        print(*matrix.pop()[::-1], end=" ")
    for row in reversed(matrix):
        if row:
            print(row.pop(0), end=" ")