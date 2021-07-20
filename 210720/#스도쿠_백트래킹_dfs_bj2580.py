import sys

# 1. '0' 인 위치를 모두 저장한다.
# 2. 유망한 숫자, 칸에 들어갈 수 있는 숫자를 골라주는 promising() 을 만든다.
# 2-1. promising 이란,
# * 해당 행, 열에 포함되지 않은 숫자
# * 해당 3 x 3 칸에 포함되지 않은 숫자
# 3. 유망한 숫자들을 집어넣는다.
# 4. 다음 0 인 곳으로 넘어간다. (재귀함수)
# 5. 해당부분을 다시 0 으로 초기화 한다. (백트래킹, 내부에서 정답이 없을 경우를 고려)
# 6. 마지막 0 까지 넣어봤다면 출력한다.


sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]


def promising(x, y):
    candidate = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        if sudoku[i][y] in candidate:
            candidate.remove(sudoku[i][y])
        if sudoku[x][i] in candidate:
            candidate.remove(sudoku[x][i])

    x //= 3
    y //= 3
    for i in range(3):
        for j in range(3):
            if sudoku[3 * x + i][3 * y + i] in candidate:
                candidate.remove(sudoku[x + i][y + i])

    return candidate


flag = False


def dfs(idx):
    global flag

    if flag:
        return

    if idx == len(zeros):
        flag = True
        for row in sudoku:
            print(*row)
        return

    (i, j) = zeros[idx]
    _candidate = promising(i, j)
    for c in _candidate:
        sudoku[i][j] = c
        dfs(idx + 1)
        sudoku[i][j] = 0


dfs(0)
