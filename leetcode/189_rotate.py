class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # ... 추가 예정 
        
        
        
        
        
    ###################
    # O(N) 
    # deque 사용 
    def f1(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n 
        
        a = deque(nums) # use additional memory. 
        while(k):
            k -= 1 
            tmp = a.pop()
            a.appendleft(tmp)
        
        for i, num in enumerate(a):
            nums[i] = num
    
    ###################
    # dict 사용 
    # O(N)
    def f2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dic = {}
        n = len(nums)
        k %= n
        
        for i, num in enumerate(nums):
            dic[(i+k)%n] = num
        
        for i in range(n):
            nums[i] = dic[i]
    
    
    ###################
    # rev 함수 선언해서 copy 진행 
    def f3(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        
        nums.reverse()
        self.rev(nums, k, n-1)
        self.rev(nums, 0, k-1)
    
    def rev(self, arr: List[int], sidx: int, eidx: int) -> None:
        while sidx < eidx:
            arr[sidx], arr[eidx] = arr[eidx], arr[sidx]
            sidx += 1
            eidx -= 1 
    ###################
    
    
