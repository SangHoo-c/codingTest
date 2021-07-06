# 1. 입력의 자릿수에 대해 2개씩 조합할 수 있는 경우를 구해놓는다
# 2. 자릿수를 K번째 까지 계속 바꾼 후 만들 수 있는 가장 큰 수를 출력한다. 만약 ans 값이 초기값인 -1e9 그대로면 만들 수 없다는 뜻이므로 -1 출력

from collections import deque
import sys, copy

input = sys.stdin.readline


# nCr 구현하기
def combination(arr, r):
    n = len(arr)
    arr = sorted(arr)
    _visited = [0] * n
    _result = []

    def dfs(x):
        # 종료 조건
        if len(x) == r:
            _x = copy.copy(x)
            _result.append(_x)
            return

        st = arr.index(x[-1]) + 1 if x else 0
        for i in range(st, n):
            x.append(arr[i])
            # _visited[i] = 1
            dfs(x)
            x.pop()
            # _visited[i] = 0

    dfs([])
    return _result


# print(combination([7, 6, 3, 1, 5], 2))


def bfs():
    _visited = set()
    _max = -1e9
    _qlen = len(q)
    while _qlen:
        x = q.popleft()
        l = list(str(x))
        for i, j in d:  # 해당 차수 (k) 에서 가능한 모든 경우 계산한다.
            s = copy.copy(l)
            s[i], s[j] = s[j], s[i]
            if s[0] == '0':
                # bfs 에서 해당 차수는 skip 한다.
                continue
            _next = int(''.join(s))
            if _next not in _visited:
                _max = max(_max, _next)
                _visited.add(_next)
                q.append(_next)
        _qlen -= 1
    return _max


n, k = map(int, input().split())
item = [i for i in range(len(str(n)))]
d = list(combination(item, 2))
q = deque()
q.append(n)

ans = 0
while k:
    ans = bfs()
    k -= 1
if ans < 0:
    print(-1)
else:
    print(ans)
