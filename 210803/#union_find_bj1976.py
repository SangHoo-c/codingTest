import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
check = list(map(int, sys.stdin.readline().split()))
root = [0] * (N + 1)
for k in range(N + 1):
    root[k] = k


def get_root(idx):
    if root[idx] == idx:
        return idx
    root[idx] = get_root(root[idx])   # 해당 부분이 중요함, root 를 거슬러 올라가며 갱신해야한다. 
    return root[idx]


def main():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                x = i + 1
                y = j + 1

                p_x = get_root(x)
                p_y = get_root(y)

                # if p_x != p_y:      # root 가 같은지 확인, root 가 다르다면 합친다.
                if p_x < p_y:
                    root[p_y] = p_x
                else:
                    root[p_x] = p_y
    # print(root)
    for i in range(len(check)-1):
        if root[check[i]] != root[check[i + 1]]:
            print("NO")
            return

    print("YES")
    return


main()
