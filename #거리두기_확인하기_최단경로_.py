import heapq

def solution(places):
    answer = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    
    for place in places:
        check_flag = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    visited = [[0 for _ in range(5)] for _ in range(5)]
                    heap = []
                    heapq.heappush(heap, [0, i, j]) # cost, i, j
                    visited[i][j] = 1
                    
                    while heap:
                        cost, r, c = heapq.heappop(heap)
                        if cost == 2:
                            break
                        for k in range(4):    # 여기!!!!! 앞에서 사용했던 i 변수를 재사용하는 실수를 했음!!!!! 이런 실수 다시 하지 않기!!!!! 
                            nx = r + dx[k]
                            ny = c + dy[k]
                            
                            if not (0 <= nx < 5 and 0 <= ny < 5):
                                continue
                            if visited[nx][ny]:
                                continue
                            if place[nx][ny] == "X":
                                continue
                            if place[nx][ny] == "P":
                                if cost < 2:
                                    print(cost, i, j, nx, ny)
                                    check_flag = 0
                                    break  
                                
                            visited[nx][ny] = 1
                            heapq.heappush(heap, [cost + 1, nx, ny])
                                
                        if not check_flag:
                            break
                if not check_flag:
                    break
            if not check_flag:
                break
        answer.append(check_flag)
          
        
    return answer
