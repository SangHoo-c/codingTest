# 자물쇠 문제
# O ( N * K * K ) 풀이이다. => 시간복잡도 초과 
import sys


def show_locks(arr, N, K):
    for i in range(K):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()


def get_min_change_in_vertical_action(arr, aimed_idx):
    L = len(arr)
    # index 5 와의 최소 비용 구하기
    min_value = 1e9
    for i in range(L):
        if int(arr[i]):
            a = L - aimed_idx + i
            b = abs(aimed_idx - i)
            min_value = min(min_value, min(a, b))
    return min_value


def main():
    my_answer = []
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        N, K = map(int, sys.stdin.readline().split(" "))
        locks = [list(str(sys.stdin.readline().strip())) for _ in range(K)]

        # show_locks(locks, N, K)
        max = -1e9
        max_candidate = []

        # O(K * N ) 으로 최댓값의 위치를 찾는다.
        for i in range(K):
            check = 0
            for j in locks[i]:
                if int(j):
                    check += 1

            if max < check:
                max_candidate = [i]
                max = check
            elif max == check:
                max_candidate.append(i)

        # max candidate 하나씩 horizontal 을 잡고 갯수를 센다.
        # 목표 index 가 정해진 상황
        min_candidates = []
        for aimed_idx in max_candidate:
            # aimed_idx = 2
            anw_list = []
            for j in range(N):
                tmp_list = []

                for i in range(K):
                    tmp_list.append(locks[i][j])
                anw_list.append(get_min_change_in_vertical_action(tmp_list, aimed_idx))
            
            min_candidates.append(sum(anw_list))
            
        my_answer.append(min(min_candidates))

    for i in range(len(my_answer)):
        print('#{}'.format(i + 1), end=" ")
        print(my_answer[i])


main()
