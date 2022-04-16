"""
기존 풀이 : tmp 변수로 swap 진행. 
python swap 은 추가 변수를 할당할 필요가 없다. 
=> but, shallow copy 이다. 
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        si = 0 
        ei = n-1 
        
        while(si <= ei):
            s[si], s[ei] = s[ei], s[si]
            
            si += 1
            ei -= 1 
