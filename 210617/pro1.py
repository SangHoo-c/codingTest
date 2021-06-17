import sys
from collections import deque

anw_list = []


def main():
    T = int(sys.stdin.readline().strip())

    for t in range(T):
        N = int(sys.stdin.readline().strip())
        time = list(map(int, sys.stdin.readline().split(" ")))
        solve(N, time)


def solve(N, time):
    anw = 0
    A = deque()
    B = deque(time)

    while 1:
        A = deque(sorted(list(A)))
        B = deque(sorted(list(B)))

        if len(B) == 1:
            anw += B.popleft()
            break
        if len(B) == 2:
            B.popleft()
            anw += B.popleft()
            break

        if len(A) == 0:
            a1 = B.popleft()
            a2 = B.popleft()
            A.append(a1)
            A.append(a2)
            anw += a2
            anw += a1

            A = deque(sorted(list(A)))
            a_min_to_b = A.popleft()
            B.append(a_min_to_b)
            B = deque(sorted(list(B)))

        else:
            b1 = B[0]
            b2 = B[1]
            a_min = A[0]
            if b2 > a_min:
                b_max_to_a_1 = B.pop()
                b_max_to_a_2 = B.pop()
                A.append(b_max_to_a_1)
                A.append(b_max_to_a_2)
                anw += max(b_max_to_a_1, b_max_to_a_2)

                A = deque(sorted(list(A)))
                a_min_to_b_ = A.popleft()
                anw += a_min_to_b_
                B.append(a_min_to_b_)
                B = deque(sorted(list(B)))

            else:
                b_min_to_a_1 = B.popleft()
                b_min_to_a_2 = B.popleft()
                A.append(b_min_to_a_1)
                A.append(b_min_to_a_2)
                anw += max(b_min_to_a_1, b_min_to_a_2)

                A = deque(sorted(list(A)))
                a_min_to_b__ = A.popleft()
                anw += a_min_to_b__
                B.append(a_min_to_b__)
                B = deque(sorted(list(B)))
    anw_list.append(anw)


main()
for i in range(len(anw_list)):
    print('#{}'.format(i+1),end=' ' )
    print(anw_list[i])
