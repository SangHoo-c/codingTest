def solution(s):
    answer = []
    arr = s[2:-2].split("},{")
    dict = {}
    for ar in arr:
        a = list(map(int, ar.split(",")))
        for ele in a:
            dict.setdefault(ele, 0)
            dict[ele] += 1
    _dict = sorted(dict.items(), key=lambda x:-x[1])
    for _d in _dict:
        answer.append(_d[0])
    
    return answer
