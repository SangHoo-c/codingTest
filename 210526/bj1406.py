from collections import deque
import sys

A = deque(sys.stdin.readline().strip())
B = deque()
N = int(sys.stdin.readline())

for _ in range(N):
    a = list(sys.stdin.readline().split())
    if a[0] == 'P':
        A.append(a[1])

    elif a[0] == 'L' and A:
        tmp = A.pop()
        B.append(tmp)

    elif a[0] == 'B' and A:
        A.pop()

    elif a[0] == 'D' and B:
        A.append(B.pop())

B.reverse()
A += B
print(''.join(A))
