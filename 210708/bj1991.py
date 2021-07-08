# output 을 원하는 모양으로 만들기,,,,, => 실수 * 4 번이나 함.. 

import sys

N = int(input())
_node = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]


# a 의 정보를 찾는 함수
def find(a):
    for i in range(N):
        if _node[i][0] == a:
            # print('find!')
            return i
    return -1


# 전위 순회
def f1(x):
    if x == '.':
        return
    print(x, end="")
    idx = find(x)
    f1(_node[idx][1])
    f1(_node[idx][2])


# 중위 순회
def f2(x):
    if x == '.':
        return
    idx = find(x)
    f2(_node[idx][1])
    print(x, end="")
    f2(_node[idx][2])


# 후위 순회
def f3(x):
    if x == '.':
        return
    idx = find(x)
    f3(_node[idx][1])
    f3(_node[idx][2])
    print(x, end="")


f1(_node[0][0])
print()
f2(_node[0][0])
print()
f3(_node[0][0])
