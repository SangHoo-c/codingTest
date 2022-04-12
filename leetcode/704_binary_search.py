"""
1. 새로운 start_index / last_index 설정시, +- 1 을 생각하지 못했다. 

+) 손으로 그려보지 않았다.  
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        si = 0 
        li = len(nums) - 1 
        result = -1 
        
        while(si <= li):
            mid = (si + li) // 2
            if nums[mid] == target:
                result = mid  
                break
            elif nums[mid] < target:
                si = mid + 1  
            elif nums[mid] > target:
                li = mid - 1 
            else:
                pass
            
        return result  
