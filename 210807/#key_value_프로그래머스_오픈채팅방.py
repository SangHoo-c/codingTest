def solution(record):
    answer = []
    name = {}
    output = []
    for rec in record:
        # command, uid, nic = rec.split(" ")
        rec_ar = rec.split(" ")
        if rec_ar[0] == 'Enter':
            name[rec_ar[1]] = rec_ar[2]
            output.append([rec_ar[0], rec_ar[1]])
        elif rec_ar[0] == 'Leave':
            output.append([rec_ar[0], rec_ar[1]])
        elif rec_ar[0] == 'Change':
            name[rec_ar[1]] = rec_ar[2]
        
    for out in output:
        if out[0] == 'Enter':
            # print(name[out[1]], end="님이 들어왔습니다.\n")
            answer.append(name[out[1]] + "님이 들어왔습니다.")
        elif out[0] == 'Leave':
            # print(name[out[1]], end="님이 나갔습니다.\n ")
            answer.append(name[out[1]] + "님이 나갔습니다.")
            
            
    
    return answer
