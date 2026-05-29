class Solution:
    def minElement(self, nums: List[int]) -> int:
        dfs = lambda n: 0 if n == 0 else n%10 + dfs(n//10)
        return min(dfs(n) for n in nums)