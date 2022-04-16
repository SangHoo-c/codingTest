"""
two pointer 로 구현이 가능하다. 

python extended slice 
arr[A:B:C]의 의미 : index A 부터 index B 까지 C의 간격으로 배열을 만들어라. 

https://docs.python.org/release/2.3.5/whatsnew/section-slices.html
"""

class Solution:    
    def reverseWords(self, s: str) -> str:
        texts = s.split(" ")
        result = []
        for t in texts:
            result.append(t[::-1])

        return " ".join(result)
            
        
