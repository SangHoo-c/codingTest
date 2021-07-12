# union find
N = 10
parent = list()
parent.append(0)
for i in range(1, N + 1):
    parent.append(i)


def get_parent(p, x):
    if p[x] == x:
        return x
    p[x] = get_parent(p, p[x])
    return p[x]


def union_parent(p, a, b):
    a = get_parent(p, a)
    b = get_parent(p, b)
    if a < b:
        p[b] = a
    else:
        p[a] = b


def find_parent(p, a, b):
    a = get_parent(p, a)
    b = get_parent(p, b)
    if a == b:
        return 1
    else:
        return 0


union_parent(parent, 1, 2)
union_parent(parent, 2, 3)
union_parent(parent, 3, 4)
union_parent(parent, 5, 6)
union_parent(parent, 6, 7)
union_parent(parent, 7, 8)
print("1과 5는 연결되어있나요? %d" % find_parent(parent, 1, 5))
union_parent(parent, 1, 5)
print("1과 5는 연결되어있나요? %d" % find_parent(parent, 1, 5))

