# 모든 경우를 순회 
# 각 점을 기준으로 4분면을 나눠 체크 

import sys

N, M, L, K = map(int, input().split())
star = []
for i in range(K):
    x, y = map(int, sys.stdin.readline().split())
    star.append([x, y])

# print(star[1])
# print(star[1][0] - star[2][0])
max_value = - 1e9
for i in range(K):
    # print("----")
    # print(star[i])

    # 1 사분면
    cnt = 0
    for j in range(K):
        if star[i][0] <= star[j][0] and star[i][1] <= star[j][1]:
            print(star)
            break

        if star[j][0] - star[i][0] <= L and star[j][1] - star[i][1] <= L:
            print(star[j])
            cnt += 1
    print("--cnt--", end=" ")
    print(cnt)
    max_value = max(max_value, cnt)

    # 2 사분면
    cnt = 0
    for j in range(K):
        if not star[i][0] >= star[j][0] or not star[j][1] >= star[i][1]:
            break

        if star[i][0] - star[j][0] <= L and star[j][1] - star[i][1] <= L:
            print(star[j])
            cnt += 1
    print("--cnt--", end=" ")
    print(cnt)
    max_value = max(max_value, cnt)

    # 3 사분면
    cnt = 0
    for j in range(K):
        if not star[i][0] >= star[j][0] or not star[i][1] >= star[j][1]:
            break


        if star[i][0] - star[j][0] <= L and star[i][1] - star[j][1] <= L:
            print(star[j])
            cnt += 1
    print("--cnt--", end=" ")
    print(cnt)
    max_value = max(max_value, cnt)

    # 4 사분면
    cnt = 0
    for j in range(K):
        if not star[i][0] <= star[j][0] or not star[i][1] >= star[j][1]:
            break


        if star[j][0] - star[i][0] <= L and star[i][1] - star[j][1] <= L:
            print(star[j])
            cnt += 1
    print("--cnt--", end=" ")
    print(cnt)
    max_value = max(max_value, cnt)

print(K - max_value)
