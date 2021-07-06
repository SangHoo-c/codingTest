# 단어수학, 리뷰
# 방법 1. 완전탐색
# 방법 2. 숫자를 이용 => 내 방법, 딕셔너리를 사용 

import sys

N = int(input())
_word = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
_dict = {}
_result = 0

for w in _word:
    _len = len(w)
    for i in range(_len):
        if w[i] in _dict:
            _dict[w[i]] += 10 ** (_len - (i + 1))
        else:
            _dict[w[i]] = 10 ** (_len - (i + 1))


_dict = sorted(_dict.items(), key= lambda x : x[1], reverse=True)

for i in range(len(_dict)):
    _mul = 9 - i
    _result += _mul * _dict[i][1]
print(_result)


