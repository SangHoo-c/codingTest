"""
  back-tracking 외워서 풀려고 하지말자. 
  흐름을 파악하자 
  1. 종료조건
  2. 재귀 진행 
"""

answer = 0


def rec(idx, numbers, target, value):
    global answer
    n = len(numbers)
    if idx == n and value == target:
        answer += 1
        return
    if idx == n:
        return

    rec(idx + 1, numbers, target, value + numbers[idx])
    rec(idx + 1, numbers, target, value - numbers[idx])


def solution(numbers, target):
    global answer
    rec(0, numbers, target, 0)
    return answer


numbers = [1, 1, 1, 1, 1]
target = 3
solution(numbers, target)

