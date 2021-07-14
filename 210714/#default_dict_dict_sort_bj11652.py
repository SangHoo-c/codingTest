import sys
from collections import defaultdict

dic = defaultdict(int)
N = int(sys.stdin.readline())
for _ in range(N):
    dic[int(sys.stdin.readline())] += 1

out = sorted(dic.items(), key=lambda x: [-x[1], x[0]])  # value 가 큰 순으로 정렬, key 가 작은 순으로 정렬 
print(out[0][0])
