def solution(N):
    # write your code in Python 3.6
    cnt = 0
    prv = 0
    cur = 0
    _max = 0
    while(N):
        cur += 1
        if N % 2 == 1:
            cnt += 1
            if prv != 0:
                _max = max(_max, cur - prv - 1)
            prv = cur

        N //= 2
    if cnt == 1:
        return 0
    return _max
