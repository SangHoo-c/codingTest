# import copy


def solution(enter, leave):
    ei = 0
    li = 0
    room = []
    answer = [[] for i in range(len(enter) + 1)]
    # result = [0] * (len(enter) + 1)

    while ei < len(enter) or li < len(leave):
        if leave[li] in room:
            room.remove(leave[li])
            li += 1
        else:
            # tmp = copy.deepcopy(room)
            # answer[enter[ei]] = tmp
            # room.append(enter[ei])
            # ei += 1
            # copy 를 사용하지 않아도 할 수 있는 풀이 
            answer[enter[ei]] = room[:]
            room.append(enter[ei])
            ei += 1

    # for p, people in enumerate(answer):
    #     result[p] += len(people)
    #     for person in people:
    #         result[person] += 1
    # return result[1:]

    for p, people in enumerate(answer):
        for person in people:
            answer[person].append(p)
    return [len(set(i)) for i in answer][1:]
  
  
  """
enter = [1,4,2,3]	
leave = [2,1,3,4]	
result = [2,2,1,3]
  """
