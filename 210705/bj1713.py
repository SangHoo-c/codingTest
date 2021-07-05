# 1 번 풀이 

import sys

input = sys.stdin.readline

N = int(input())
W = int(input())
num = list(map(int, input().split(" ")))

# key : 후보자 id
# value : [추천수 , 들어온 순서]
photo = dict()
for i in range(W):
    if num[i] in photo:
        photo[num[i]][0] += 1
    else:
        if len(photo) < N:
            photo[num[i]] = [1, i]
        else:
            del_list = sorted(photo.items(), key=lambda x: (x[1][0], x[1][1]))
            del_key = del_list[0][0]
            print(del_list[0])
            del (photo[del_key])
            photo[num[i]] = [1, i]

ans_list = list(sorted(photo.keys()))
answer = str(ans_list[0])
for i in ans_list[1:]:
    answer += " " + str(i)
print(answer)



# -------------------------------
# 2 번 풀이 


N = int(input()) # 사진틀 개수
Vote = int(input()) # 총 추천 회수
students = list(map(int, input().split())) # 추천 학생 번호
picture = [] # 사진틀
score = [] # 사진틀 인덱스와 매치해서 추천수 저장할 리스트

for i in range(Vote):
    if students[i] in picture: # 사진틀에 있으면
        for j in range(len(picture)): #이부분 N으로 놓고 계속 틀렸음.. ㅋㅋㅋㅋㅋ
            if students[i] == picture[j]:
                score[j] += 1 #점수증가
    else: # 사진틀에 없고
        if len(picture) >= N: # 사진틀 꽉차있으면
            for j in range(N):
                if score[j] == min(score): #가장 작은 점수 찾고
                    del picture[j]
                    del score[j]
                    break #먼저 찾으면 스탑 왜냐면 오래된거일수록 인덱스 앞에 있음
        picture.append(students[i]) #새로운거 뒤에 더해줌
        score.append(1)

picture.sort()
print(' '.join(map(str, picture)))


