# 시간초과가 난 경우 
# O(N^2), N <= 2^15 이므로 시간 초과 
# 재귀를 모든 경우 반복하는게 문제 

N, r, c = map(int, input().split())
cnt = -1


def rec(i, j, L):
    global cnt
    if L == 2:
        cnt += 1
        if r == i and c == j:
            return cnt

        cnt += 1
        if r == i and c == j + 1:
            return cnt

        cnt += 1
        if r == i + 1 and c == j:
            return cnt

        cnt += 1
        if r == i + 1 and c == j + 1:
            return cnt

    elif L > 2:
        L_ = L // 2

        a = rec(i, j, L_)
        b = rec(i, j + L_, L_)
        C = rec(i + L_, j, L_)
        d = rec(i + L_, j + L_, L_)

        if a:
            return a
        if b:
            return b
        if C:
            return C
        if d:
            return d

    else:
        print("wrong input")
        return 0


print(rec(0, 0, 2 ** N))
