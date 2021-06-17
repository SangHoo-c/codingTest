import sys

final_list = []
answer_list = []
anw = 0


def solve(a, b):
    global final_list
    anw_value = 0
    for k in range(len(a) - 1):
        while a[k] != 0:

            # switching 케이스에 대한 flag
            if a[k] * b[0] >= 0:  # 같은 부호 일때
                sw_flag = 1
            else:  # 다른 부호 일때
                sw_flag = 0

            res = []
            for j in range(k):
                res.append(0)

            if a[k] == 0:
                break
            for i in range(k, len(a)):

                if i < len(b) + k:
                    # res.append(a[i] + b[i - k])     # switching 케이스까지 생각해야한다.
                    if sw_flag == 0:  # 다른 부호 일때
                        res.append(a[i] + b[i - k])  # switching 케이스까지 생각해야한다.
                    elif sw_flag == 1:  # 같은 부호 일때
                        res.append(a[i] - b[i - k])  # switching 케이스까지 생각해야한다.
                    else:
                        print("@@@@")
                else:
                    res.append(a[i])
            # print(res)
            anw_value += 1
            a = res
            final_list = res
            # print(anw_value)
    return anw_value


def main():
    global anw
    # global final_list
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        # print('{} 번쨰 '.format(t+1))
        A_str = list(map(str, sys.stdin.readline().split(" ")))
        A = []
        a = A_str[0]
        b = A_str[1]
        if len(a) < len(b):
            anw = -1
            break
        for i in range(len(b)):
            A.append(int(a[-i - 1]) - int(b[-i - 1]))
        for j in range(len(b), len(a)):
            A.append(int(a[-j - 1]))
        A.reverse()
        # print(A)

        B_str = list(map(str, sys.stdin.readline().strip()))
        B = []
        for b in B_str:
            if b == '+':
                B.append(1)
            elif b == '0':
                B.append(0)
            elif b == '-':
                B.append(-1)
            else:
                print('wrong input')
        # print(B)
        # 구현부
        
        
        
        anw = 0
        for check in B:
            if check:
                if B[0] == 0:
                    B.reverse()

                anw += solve(A, B)
                final_list.reverse()
                A = final_list

                if final_list:
                    anw += solve(final_list, B)

                if final_list[-1] != 0:
                    anw = -1
                    # print('wrong input!!! return -1')
        answer_list.append(anw)
        # print('-----')


main()
for i in range(len(answer_list)):
    print('#{}'.format(i + 1), end=" ")
    print(answer_list[i])
