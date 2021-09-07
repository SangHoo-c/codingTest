""" 
  isdigit()
  eval()
  join() 등등, 
  
  문자열 관련 함수들 사용법 익히기. 
"""

from itertools import permutations


def cal(pri, idx, exp):
    if exp.isdigit():
        return str(exp)
    else:
        if pri[idx] == "*":
            s_exp = exp.split("*")
            temp = []
            for s in s_exp:
                temp.append(cal(pri, idx + 1, s))
            return str(eval("*".join(temp)))

        elif pri[idx] == "+":
            s_exp = exp.split("+")
            temp = []
            for s in s_exp:
                temp.append(cal(pri, idx + 1, s))
            return str(eval("+".join(temp)))

        elif pri[idx] == "-":
            s_exp = exp.split("-")
            temp = []
            for s in s_exp:
                temp.append(cal(pri, idx + 1, s))
            return str(eval("-".join(temp)))


def solution(expression):
    answer = 0
    operand = set()
    for ep in expression:
        if ep in {'-', '+', '*'}:
            operand.add(ep)

    priorities = list(permutations(list(operand), len(operand)))

    for p in priorities:
        answer = max(abs(int(cal(p, 0, expression))), answer)

    return answer

