class Solution:
    # failed
    def f1(self, nums: List[int]) -> None:        
        n = len(nums)
        
        for i in range(n):                
            if(nums[i] == 0):
                if i == n-1:
                    pass
                nums[i:] = nums[i+1:]
                nums.append(0)
                
                for j in range(i, n):
                    if(nums[i] == 0):
                        nums[i:] = nums[i + 1:]
                        nums.append(0)

    # successed but not good at performance 
    def f2(self, nums: List[int]) -> None:
        n = len(nums)
        for i in range(n):
            si, li = i, i
            if nums[si] == 0:
                while(li < n - 1  and nums[li] == 0):
                    li += 1 
                nums[si:] = nums[li:]
                # nums.append([0 for i in range(li - si)])  # add ele to list 
                nums.extend([0 for i in range(li - si)])    # add list to list 
                
    # successed. faster than f2.              
    def f3(self, nums):
        append_times=nums.count(0)
        for i in range(append_times):
            nums.remove(0) # Delete the front zero
            nums.append(0) # append it at the end of nums, the times of the addition and substraction shall be equal
    
    
    ##################################################
    # best answer. fast / effcient 
    def f4(self, nums: List[int]) -> None:
        pos = 0
        
        for i, num in enumerate(nums):
            if num != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
    ##################################################
                
                    
                
                   
                
        
