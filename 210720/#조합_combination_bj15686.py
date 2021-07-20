import sys

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

chicken = []
house = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append([i + 1, j + 1])
        elif arr[i][j] == 2:
            chicken.append([i + 1, j + 1])
        else:
            continue

# nCr 조합 구하기
c_len = len(chicken)
c_arr = []  # chicken 집 전체중에 M 개를 뽑아 저장할 배열  
visited = [0] * c_len
final_value = 1e9


# nCm
def dfs():
    global final_value
    if len(c_arr) == M:
        final_value = min(final_value, calculate(c_arr))

    _st = chicken.index(c_arr[-1]) if c_arr else 0
    for i in range(_st, c_len):
        if chicken[i] not in c_arr and visited[i] == 0:
            visited[i] = 1
            c_arr.append(chicken[i])
            dfs()
            visited[i] = 0
            c_arr.pop()


# 뽑아진 조합으로 계산한 치킨 거리 (거리의 합)
def calculate(ar):
    _result = []
    _value = 1e9
    for a, b in house:
        _min = 1e9
        for x, y in ar:
            _min = min(_min, abs(a - x) + abs(b - y))
        _result.append(_min)
    return sum(_result)


dfs()
print(final_value)
