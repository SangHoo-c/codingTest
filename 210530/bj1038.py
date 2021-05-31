# 1~ 1,000,000 의 모든 경우를 계산해서 가능한 경우, cnt 를 증가시키는 Brute-force 풀이 
# 대부분의 예외 케이스를 테스트 해봤지만, 통과하지 못한 풀이
# 백트래킹 방법을 사용하여 다시 풀어보려고 한다. 

def func(i):
    input_num = str(i)
    input_len = len(input_num)
    vis = []
    vis.append(i % 10)
    cnt = 1

    for j in range(1, input_len):
        if i % 10 ** (j + 1) // 10 ** j <= vis[j - 1]:
            break
        else:
            vis.append(i % 10 ** (j + 1) // 10 ** j)
            cnt += 1
    if cnt == input_len:
        # print("감소하는 수 인정!")
        return 1
    return 0


def solution(N):
    min_cnt = -1
    for i in range(1000001):
        if func(i):
            min_cnt += 1
        if N == min_cnt:
            print(i)
            return 0
    print(-1)



N = int(input())
solution(N)
