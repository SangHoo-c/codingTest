import sys

N = int(sys.stdin.readline().strip())
weight = list(map(int, sys.stdin.readline().split(" ")))
max = 1
weight.sort()
# sorted(weight, key= lambda x : x)
# print(weight)

for i in range(N):
    if max >= weight[i]:
        max += weight[i]
    else:
        # max += 1
        break
print(max)
