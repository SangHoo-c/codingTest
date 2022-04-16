"""
1. O(N) heap 사용 
2. O(N) two-pointer : 초기 입력값이 오름차순이기에 가능 O(N)
"""

import heapq 

class Solution:
    # heap 사용 풀이 
    def sortedSquaresHeapQ(self, nums: List[int]) -> List[int]:
        heap = []
        result = []
        
        for num in nums:
            heapq.heappush(heap, num**2)
        
        while(heap):
            result.append(heapq.heappop(heap))
        
        return result 
      
      # two-pointer 사용 풀이 
      def sortedSquaresTwoPointer(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = 0
        e = n - 1 
        idx = n - 1
        result = [0] * (n)
        
        while(idx >= 0):
            if(nums[s]**2 > nums[e]**2):
                result[idx] = nums[s]**2
                s += 1 
            else:
                result[idx] = nums[e]**2
                e -= 1 
            idx -= 1 
        
        return result 
            
            
            
        
