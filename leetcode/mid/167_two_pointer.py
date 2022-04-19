class Solution:           
    # O(N^2) time limit 
    def f1(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            for j in range(i+1, n):               
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
                  
                  
    ############################################################
    # most efficient answer. 
    # O(N) two-pointer
    def f2(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1 
        while l < r:
            s = numbers[l] + numbers[r]
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                return [l + 1, r + 1]
    ############################################################
    
    # O(N) dict 
    # 중복 제거하기 위해서, 검사 후 값 insert 진행
    def f3(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i 
    
    # O(logN)
    # binary-search             
    def f4(self, numbers: List[int], target: int) -> List[int]:
        li = 0
        ri = len(numbers) - 1 
        
        while li < ri:
            mid = numbers[li] + numbers[ri]
            if mid == target:
                return [li+1, ri+1]
            elif mid < target:
                li += 1
            elif mid > target:
                ri -= 1 
            else:
                pass
            
            
