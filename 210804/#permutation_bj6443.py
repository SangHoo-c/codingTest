import sys

N = int(input())

for _ in range(N):
    arr = []
    s = list(map(str, sys.stdin.readline().strip()))
    visited = [0] * (len(s) + 1)
    s.sort()
    s_len = len(s)


    def per():
        if len(arr) == s_len:
            for p in arr:
                print(p, end="")
            print()
            return

        for i in range(s_len):
            if visited[i] == 0 and (i == 0 or s[i - 1] != s[i] or visited[i - 1]):
                arr.append(s[i])
                visited[i] = 1
                per()
                arr.pop()
                visited[i] = 0


    nCr()

    
    
    """
1
abc

abc
acb
bac
bca
cab
cba
    
    """
