"""
TLE solved
1. queue 에 값을 담아두는 방식 => set 을 사용해서 중복된 값을 제거하는 방식 

"""

from collections import deque


def print_arr(ar):
    for i in range(a):
        for j in range(b):
            print(ar[i][j], end=" ")
        print()
    print("-----")


def solution(m, n, board):
    answer = 0
    check_set = set()
    arr = [['0' for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            arr[i][j] = board[i][j]

    # 2x2 블록 조건에 맞는지 확인 후, 조건에 부합할 시 집합에 해당 인덱스를 추가하는 함수
    def check(b):
        for i in range(m - 1):
            for j in range(n - 1):
                if b[i][j] == b[i + 1][j] == b[i][j + 1] == b[i + 1][j + 1] != '0':
                    check_set.add((i, j))
                    check_set.add((i + 1, j))
                    check_set.add((i, j + 1))
                    check_set.add((i + 1, j + 1))

    # 격자를 다시 재배열하는 함수
    def arrange(b):
        for j in range(n):
            for i in range(m):
                if b[i][j] == '0':
                    for k in range(i, -1, -1):
                        b[k][j] = b[k - 1][j]

    while True:
        # check 함수를 통해 공백이 생기는곳 위치(인덱스) 기록
        check(arr)

        # 만약 공백이 있다면
        if check_set:
            # 공백 기록
            for i, j in check_set:
                arr[i][j] = '0'
            # 답에 공백 갯수 추가
            answer += len(check_set)

            # 공백을 기록했으니, 격자 재배열
            arrange(arr)

            # 다음 기록을 위해 집합 비우기
            check_set.clear()
        # 공백이 없다면
        else:
            # 더 이상 점수를 얻을수 없으니 반복문 탈출
            break

    return answer

"""
a = 6
b = 6
c = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(a, b, c))
"""
