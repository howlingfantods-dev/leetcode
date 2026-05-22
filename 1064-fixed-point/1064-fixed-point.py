class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        n = len(arr)
        l,r,ans = 0, n, -1
        while l < r:
            m = l + (r - l)//2
            if arr[m] == m:
                ans = m
            if arr[m] < m:
                l = m + 1
            else:
                r = m
        return ans