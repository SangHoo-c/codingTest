import sys
sys.setrecursionlimit(10**6)
arr = []


def main():
    N = int(input())
    left = 0
    right = 0
    arr.append(int(sys.stdin.readline()))
    print(arr[0])  # 1 번째 값 출력
    for idx in range(1, N):
        x = int(sys.stdin.readline())
        bin_search(left, right, x)
        right += 1
        if idx % 2 == 1:
            print(arr[idx // 2])
        else:
            print(max(arr[idx // 2], arr[(idx // 2) - 1]))


def bin_search(l, r, x):
    _mid = (l + r) // 2
    if l == r:
        # print('자리 찾음')
        if arr[l] < x:
            arr.insert(l + 1, x)
        else:
            arr.insert(l, x)
        return

    if x == arr[_mid]:
        # print('같은 값 찾음')
        arr.insert(_mid, x)
        return
    elif x < arr[_mid]:
        bin_search(l, _mid - 1, x)
    elif x > arr[_mid]:
        bin_search(_mid + 1, r, x)


main()
