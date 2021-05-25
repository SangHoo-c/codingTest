from collections import deque

N = int(input())
a = deque(map(int, range(1, N + 1)))

while len(a) > 1:
    a.popleft()
    tmp = a.popleft()
    a.append(tmp)

print(a[0])
