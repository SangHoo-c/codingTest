# 오름차순의 경우, 중복체크를 할 필요가 없다. 
# 비교만 수행하면 된다. 

n, m = map(int, input().split())

arr = [0] * (m+1)       # 가능한 경우의 수를 담을 배열 

def dfs(x):
    if x == m+1:
        for i in range(1, m + 1):
            print(arr[i], end=' ')
        print()
    else:
        for i in range(1, n+1):     # 모든 경우(자식 노드)에 대해 
            if arr[x-1] < i:        # 가능여부를 체크, promising() 역할을 한다.    
                arr[x] = i
                dfs(x+1)
                arr[x] = 0
dfs(1)
