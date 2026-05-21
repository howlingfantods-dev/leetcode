class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        A=set()
        ans = 0
        DIV = len(arr1)
        for i,n in enumerate(arr1+arr2):
            while n:
                if DIV > i:A.add(n)
                if DIV <= i and n in A:
                    ans = max(ans, int(log10(abs(n)))+1)
                n//=10
        return ans

