# O(N^2) 풀이
# N <= 64 
# divide & conquer 정석적인 문제 
# bj 1074 와 비교했을때, divide 들어가기 위한 조건을 신경쓰지 않아도 괜찮았다. 
# issue 1. '(', ')' 를 언제 출력해야할지 고민했다. 

N = int(input())

image = [list(map(int, input())) for _ in range(N)]


def rec(i, j, l):
    l_div = l // 2
    b_cnt = 0
    w_cnt = 0

    block = []

    # 0. 종료시점
    if l == 1:
        return

    # 1. 해당 구역이 압축가능 지점인지
    for x in range(i, i + l):
        for y in range(j, j + l):
            if image[x][y] == 1:
                b_cnt += 1
                block.append(1)
            elif image[x][y] == 0:
                w_cnt += 1
                block.append(0)
            else:
                # print("error code #1. wrong input image. ")
                continue

    if b_cnt == l ** 2:
        print(1, end='')
        return
    elif w_cnt == l ** 2:
        print(0, end='')
        return
    elif l == 2:
        print('(', end='')
        for z in range(len(block)):
            print(block[z], end='')
        print(')', end='')
        return
    else:
        # print("error code #2. check your image array. ")
        continue

    # 2. divide
    print('(', end='')
    rec(i, j, l_div)
    rec(i, j + l_div, l_div)
    rec(i + l_div, j, l_div)
    rec(i + l_div, j + l_div, l_div)
    print(')', end='')


rec(0, 0, N)
