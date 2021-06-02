# O(n^2) 풀이 
# w_cnt, b_cnt, block 와 같은 추가적인 선언 없이 가능한 풀이 

import sys
input = sys.stdin.readline

N = int(input())
image = [list(map(int, input().strip())) for _ in range(N)]

def quadtree(x, y, n):
    # 크기 1x1
    if(n==1):
        return str(image[x][y])
    
    result =[]
    for i in range(x, x+n):
        for j in range(y, y+n):
            # 해당 구역에서 일어날 수 있는 경우를 체크 
            if(image[i][j] != image[x][y]):
                # extend는 list, tuple, dict 등의 iterable object를
                # list 끝에 append
                result.append('(')
                result.extend(quadtree(x, y, n//2))
                result.extend(quadtree(x, y+n//2, n//2))
                result.extend(quadtree(x+n//2, y, n//2))
                result.extend(quadtree(x+n//2, y+n//2, n//2))
                result.append(')')

                return result
    return str(image[x][y])


print(''.join(quadtree(0, 0, N)))
