arr = ['A', 'A', 'B', 'C', 'D']
n = len(arr)
m = 2

# nCm 구현하기
c_arr = []
visited = [0] * n
arr.sort()


def nCr():
    if len(c_arr) == m:
        print(c_arr)
        return
    st = arr.index(c_arr[-1]) if c_arr else 0
    for i in range(st, n):
        # if visited[i] == 0:
        if visited[i] == 0 and (i == 0 or arr[i - 1] != arr[i] or visited[i - 1]):  # 중복제거하는 코드 
            visited[i] = 1
            c_arr.append(arr[i])
            nCr()
            visited[i] = 0
            c_arr.pop()


nCr()
