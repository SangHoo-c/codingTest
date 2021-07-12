# 정확한 값을 찾아서 remove 하지 않고, 순서만 지켜서 pop 해주자. 

import sys

def first(n, k):
    global factorial, ori, ret
    for i in range(1, n + 1):
        a = float(k) / factorial[n-i]
        index = int(a) if a == int(a) else int(a) + 1
        ret.append(ori.pop(index - 1))      # 여기!!!!! 
        k -= (index - 1) * factorial[n-i]

def second(n):
    global problem, factorial
    s = 1
    for i in range(1, n):
        p = problem[i]
        inc = p - 1
        for j in range(1, i):
            if problem[j] < p:
                inc -= 1
        inc *= factorial[n-i]
        s += inc
    return s

n = int(sys.stdin.readline().strip())

problem = list(map(int, sys.stdin.readline().split()))

factorial = [1]
ret = []
ori = []
for i in range(n):
    ori.append(i+1)

for i in range(1, 21):
    factorial.append(factorial[-1] * i)

if problem[0] == 1:
    first(n, problem[1])
    sys.stdout.write(' '.join(map(str, ret))+'\n')
else:
    sys.stdout.write(str(second(n))+'\n')
