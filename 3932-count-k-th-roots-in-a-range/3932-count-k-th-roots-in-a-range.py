class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        ans = 0
        x = 0
        while True:
            curr = x**k
            if curr > r:break
            if l<= curr <=r:ans+=1
            x+=1
        return ans