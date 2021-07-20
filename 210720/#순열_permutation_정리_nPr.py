arr = ['A', 'A', 'B', 'C', 'D']
n = len(arr)
r = 2

# nPr 구현하기
p_arr = []
visited = [0] * n

arr.sort()


def nPr(x):
    if len(p_arr) == r:
        print(p_arr)
        return

    for i in range(n):  # 순열은 모든 케이스를 다시 돌아본다.
        if visited[i] == 0 and (i == 0 or arr[i - 1] != arr[i] or visited[i - 1]):  # 중복 제거하는 코드
            # if visited[i] == 0:
            visited[i] = 1
            p_arr.append(arr[i])
            nPr(x + 1)
            visited[i] = 0
            p_arr.pop()


nPr(0)
