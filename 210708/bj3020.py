import sys

# 각 구간의 시작점과 끝점을 체크한다, 
# +1, -1 을 해서 O(N*H) 의 시간 복잡도를 줄여준다.

N, H = map(int, sys.stdin.readline().split(" "))
_sum = [0] * 500001
for i in range(N):
    _bar = int(sys.stdin.readline())
    if i % 2 == 0:   # 석순을 구하는 과정 
        _sum[1] += 1
        _sum[_bar + 1] -= 1
    else:           # 종류석을 구하는 과정 
        _sum[H - _bar + 1] += 1

_answer = 1e9
_count = 0
for i in range(1, H + 1):
    _sum[i] += _sum[i - 1]      # 누적합을 구하는 과정 
    if _answer > _sum[i]:
        _answer = _sum[i]
        _count = 1
    elif _answer == _sum[i]:
        _count += 1

print(_answer, _count)
