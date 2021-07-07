import sys

X, Y = map(int, sys.stdin.readline().split(" "))


def main():
    s = 1
    e = 1e9
    answer = 0
    Z = Y * 100 // X
    if Z == 100 or Z == 99:
        print(-1)
        return
    while s <= e:
        mid = int((s + e) // 2)
        _next = (Y + mid) * 100 // (X + mid)
        if Z < _next:
            answer = mid
            e = mid - 1
        else:
            s = mid + 1

    print(answer)


main()
