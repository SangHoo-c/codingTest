# N-Queen 문제 
# 핵심은 가지치기를 잘 하는 것이다. 
# 거슬러 올라가는 방법 x 
# 가능성(promising)이 있는 경우, 계속 파고들고 
# 가능성(promising)이 없는 경우, 그 자리에서 멈춘다. 

N = int(input())
row = [0] * N
result = 0


# 내 윗줄에 나와 겹치는 라인에 퀸이 있는가?
def promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True


# 한줄씩 재귀하며 DFS를 실행
def dfs(x):
    global result

    if x == N:
        result += 1

    else:
        for i in range(N):
            row[x] = i         # 가능한 모든 경우를 넣어본다. 
            if promising(x):   # 해당 노드가 부모노드로서 자격이 있는지 확인한다. 
                dfs(x + 1)     # 자식 노드로 이어간다. 
                               # if 문을 통과하지 못할 경우, 다음 노드에게 부모노드의 자격을 확인한다. 


dfs(0)
print(result)
