# 1. 정렬 + 조합 
# 2. 가능한 케이스 모두 체크 
# 3. 조건에 맞는지 체크 

import copy
import sys

L, C = map(int, sys.stdin.readline().split())
cand = list(map(str, sys.stdin.readline().strip().split(" ")))

cand = sorted(cand)
cand_len = len(cand)
visited = [0] * cand_len
arr = []
result = []


def dfs(x):
    if len(arr) == L:
        _arr = copy.copy(arr)
        result.append(_arr)
        return

    st = cand.index(arr[-1]) + 1 if arr else 0       # 핵심!!!!! 조합만들때 반복제거하는 방법!!!!!!! 
    for i in range(st, cand_len):
        if not visited[i]:
            visited[i] = 1
            arr.append(cand[i])
            dfs(x + 1)
            visited[i] = 0
            arr.pop()


def chomd_num(arr):
    result = ''
    for a in arr:
        result += a
    return result


def main():
    dfs(0)
    _moum = {'a', 'e', 'i', 'o', 'u'}
    _final = []
    for password in result:
        m_flag = 0  # 모음 flag
        j_flag = 0  # 자음 flag
        for p in password:
            if p in _moum:
                m_flag += 1
            else:
                j_flag += 1
        if m_flag >= 1 and j_flag >= 2:
            _final.append(chomd_num(password))
    for anw in _final:
        print(anw)


main()
