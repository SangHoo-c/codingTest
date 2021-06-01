# 개선된 알고리즘 
# 큰 덩어리부터 생각한다. 
# 기준점, 좌상단의 꼭짓점을 기준으로 해당 구역에 (r, c) 가 들어올 수 있는지 확인한다. 

N, r, c = map(int, input().split())
cnt = 0


def rec(l, i, j):
    global cnt

    if i == r and j == c:
        print(cnt)
        return

    if l == 1:
        cnt += 1
        return

    if not (i <= r < i + l and j <= c < j + l):
        cnt += l ** 2
        return

    # dividing
    l_div = l // 2
    rec(l_div, i, j)
    rec(l_div, i, j + l_div)
    rec(l_div, i + l_div, j)
    rec(l_div, i + l_div, j + l_div)


rec(2 ** N, 0, 0)
