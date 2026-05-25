class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        counts = [0] * 101
        ans = []

        for i in range(len(nums)):
            if counts[nums[i]] < k:
                ans.append(nums[i])
                counts[nums[i]]+=1
        print(counts)
                
        return ans 