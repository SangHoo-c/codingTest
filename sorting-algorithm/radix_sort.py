# 핵심 아이디어. 
# 가공한 list 를 넣으면 안된다. 
# 날것의 list 를 다시 함수 안에 넣어줘야한다. 

from math import log 

def radix_sort(list, base=10):
    # 입력된 리스트 가운데 최대값의 자릿수 확인
    # digit = int(log(max(list), base) + 1)
    digit = len(str(max(list)))

    # 자릿수 별로 counting sort
    for d in range(digit):
        list = counting_sort_with_digit(list, d, base)  # 핵심 아이디어 구현부, list 원래 그 모습 그대로 다시 넣어준다. 
    return list


# 현재 자릿수(d)와 진법(base)에 맞는 숫자 변환
# ex) 102, d = 0, base = 10  => return:  2
def get_digit(number, d, base):
    return (number // base ** d) % base


# 자릿수 기준으로 counting sort
# arr : input array
# O : output array
# C : counting array
# base : 10진수라면 base = 10
def counting_sort_with_digit(arr, d, base):
    # k : ex) 10진수의 최대값 = 9
    k = base - 1
    O = [-1] * len(arr)
    C = [0] * (k + 1)

    # 현재 자릿수를 기준으로 빈도수 세기
    for a in arr:
        C[get_digit(a, d, base)] += 1

    # C 업데이트
    for i in range(k):
        C[i + 1] += C[i]

    # 현재 자릿수를 기준으로 정렬
    for j in reversed(range(len(arr))):     
        O[C[get_digit(arr[j], d, base)] - 1] = arr[j]
        C[get_digit(arr[j], d, base)] -= 1
    
    # return output array 
    return O


print(radix_sort([134, 245, 23]))
