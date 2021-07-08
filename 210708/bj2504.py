# 정말 오래걸렸던 문제
# stack 에 다시 넣어주는 조건을 잘 체크해야한다. 
# append 를 어느곳에서 해줘야할지, 
# 중간에 계산된 숫자를 다시 넣어주는 과정을 잘 수행해야한다. 

import sys

gual = list(map(str, sys.stdin.readline().strip()))

_stack = []
_result = 0

for g in gual:
    # 예외처리
    if (g == ']' or g == ')') and not _stack:
        print(0)
        exit()

    if g == '(' or g == '[':
        _stack.append(g)

    elif g == ')':
        _store = 0
        while _stack:
            _x = _stack.pop()
            if _x == '[':
                print(0)
                exit()
            elif _x == '(':
                if _store == 0:
                    _store = 1
                _store *= 2
                _stack.append(_store)
                break
            else:
                _store += _x

    elif g == ']':
        _store = 0
        while _stack:
            _x = _stack.pop()
            if _x == '(':
                print(0)
                exit()
            elif _x == '[':
                if _store == 0:
                    _store = 1
                _store *= 3
                _stack.append(_store)
                break
            else:
                _store += _x
          # _stack.append(_store). => 기존에 append 가 있던 위치, 모든 경우를 다 넣어주고 있다. 
                

    # print(_stack)
    else:
        print(0)
        exit()

print(0 if '(' in _stack or '[' in _stack else sum(_stack))
