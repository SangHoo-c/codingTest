# 백트래킹의 정석
n, m = map(int, input().split())

vis = [0] * (n+1)       # 방문 여부 확인 
arr = [0] * (m+1)       # 가지별 가능한 수열 

# 모든 자식 노드를 확인할때, 가능한지 확인하는 함수 
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
        for i in range(1,n+1):      # 가능한 모든 노드 확인 
            if promising(i):        # promising 함수를 통해 가능여부 체크 
                vis[i] = 1
                arr[x] = i
                dfs(x+1)            # 자식 노드로 내려간다. 
                vis[i] = 0          # 다시 부모노드로 올라간다. 
                arr[x] = 0          

dfs(1)         
