from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for num in course:
        res = []
        for order in orders:
            order = sorted(order)
            res.extend(combinations(order, num))
        counter = Counter(res)
        s_counter = sorted(counter.items(), key=lambda x: -x[1])
        _max = 2

        for key, value in s_counter:
            if value >= _max:
                _max = value
                answer.append("".join(key))

    answer.sort()
    return answer


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
solution(orders, course)
