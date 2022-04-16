# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        si = 1
        li = n
        while si <= li:
            mid = (si + li) // 2 
            if isBadVersion(mid):
                li = mid - 1 
            else:
                si = mid + 1 
        return si
            
            
