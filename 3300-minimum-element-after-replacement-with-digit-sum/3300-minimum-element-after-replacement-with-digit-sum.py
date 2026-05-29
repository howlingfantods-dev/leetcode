class Solution:
    def minElement(self, nums: List[int]) -> int:
        def dfs(n):
            if n == 0: return 0
            return n % 10 + dfs(n//10)
        return min(dfs(n) for n in nums)