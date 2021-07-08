# default dict 연습 문제 

import sys
from collections import defaultdict

check = 0
_tree = defaultdict(int)

while True:
    _name = str(sys.stdin.readline().strip())
    if _name:
        _tree[_name] += 1
        check += 1
    else:
        break

_total = len(_tree)
_tree = sorted(_tree.items(), key=lambda x:x[0])

for _item in _tree:
    out = _item[1] * 100 / check
    print(f'{_item[0]} {out:.4f}')
    # print(_item[0], end=" ")
    # print('%.4f' % out)






