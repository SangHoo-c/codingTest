n, m = map(int, input().split())

vis = [0] * (n+1)       # 방문을 체크하는 배열
arr = [0] * (m+1)       # 가능한 경우의 수를 담을 배열 

def promising(idx, num):  # 가능한 경우를 체크하는 함수 
    if vis[num] == 0 and arr[idx-1] < num:
        return True
    else:
        return False

def dfs(x):
    if x == m+1:
        for i in range(1, m + 1):
            print(arr[i], end=' ')
        print()
    else:
        for i in range(1, n+1):     # 모든 경우(자식 노드)에 대해 
            if promising(x, i):     # 가능여부를 체크 
                vis[i] = 1
                arr[x] = i
                dfs(x+1)
                vis[i] = 0
                arr[x] = 0
dfs(1)
