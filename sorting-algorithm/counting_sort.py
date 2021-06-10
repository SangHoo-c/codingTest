def counting(arr, k):
    # counting array, C
    C = [0] * (k + 1)

    # output array, O
    O = [0] * len(arr)

    # arr 에 나온 요소들 빈도수 체크
    for i in range(len(arr)):
        C[arr[i]] += 1

    # counting array 누적하기
    for i in range(k):
        C[i + 1] += C[i]

    # for i in range(len(arr)):
    # 역순으로 output 배열에 넣는 이유는 stable 한 정렬을 구현하기 위함이다.
    # 누적된 값은 output 배열의 index 이다.
    for i in reversed(range(len(arr))):
        O[C[arr[i]] - 1] = arr[i]
        C[arr[i]] -= 1

    # 결과 비교
    print(O)
    print(sorted(arr))


a = [2, 0, 2, 0, 4, 1, 5, 5, 2, 0, 4, 3]
counting(a, 5)
