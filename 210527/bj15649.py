n, m = map(int, input().split())

vis = [0] * (n+1)
arr = [0] * (m+1)

def promising(idx):
    if vis[idx] == 0:
        return True
    else:
        return False

def dfs(x):
    if x == m+1:
        for i in range(1,m+1):
            print(arr[i], end=' ')
        print()
    else:
        for i in range(1,n+1):
            if promising(i):
                vis[i] = 1
                arr[x] = i
                dfs(x+1)
                vis[i] = 0
                arr[x] = 0

dfs(1)
