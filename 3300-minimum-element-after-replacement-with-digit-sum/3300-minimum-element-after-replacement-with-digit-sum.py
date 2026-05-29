class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = inf
        for i in range(len(nums)):
            res = 0
            n = nums[i]
            while n > 0:
                res += n % 10
                n//=10 
            ans = min(ans,res)
        return ans
                