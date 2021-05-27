def dfs(x, m, n, arr):
    if x == m+1:
        for i in range(1, m + 1):
            print(arr[i], end=' ')
        print()
    else:
        for i in range(1, n+1):
            # if arr[x-1] <= i:     중복을 허용하여, promising() 이 필요가 없어졌다. 
            arr[x] = i
            dfs(x+1, m, n, arr)
            arr[x] = 0

def solution():
    n, m = map(int, input().split())
    arr = [0] * (m + 1)
    dfs(1, m, n, arr)

solution()
