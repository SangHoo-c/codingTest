# -*- coding: utf-8 -*-
import sys

T = int(sys.stdin.readline())  # 테스트케이스 갯수
for i in range(T):
    count = 1
    people = {}
    N = int(sys.stdin.readline()) # 명수
    for j in range(N):
        Paper, Interview = map(int, sys.stdin.readline().split())
        people[Paper] = Interview
    sorted(people.items())

    Max = people[1]

    for key in people:
        if Max > people[key]:
            Max = people[key]
            count += 1

    print(count)
