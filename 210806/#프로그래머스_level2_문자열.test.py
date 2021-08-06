def solution(n, words):
    answer = []
    idx = 0
    word_set = set()
    exit_flag = False
    prev_word = ''
    while True:
        for i in range(1, 1 + n):
            if idx == len(words):
                answer = [0, 0]
                exit_flag = True
                break
            elif words[idx] not in word_set:
                if prev_word == '' or words[idx][0] == prev_word[-1]:
                    prev_word = words[idx]
                else:
                    answer = [i, idx // n + 1]
                    exit_flag = True
                    break
                word_set.add(words[idx])

            else:
                answer = [i, idx // n + 1]
                exit_flag = True
                break
            idx += 1
        if exit_flag:
            break

    return answer


n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n, words))
