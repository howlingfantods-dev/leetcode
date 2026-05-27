class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        def dfs(i,c):
            if i == len(word):
                return 0

            res = 0
            diff = ord(word[i]) 
            if word[i].islower():
                diff -= ord('a')
                if c[diff] == 0: c[diff]+=1
                if c[diff] == 2:
                    c[diff]= -1
                    res-=1

            if word[i].isupper():
                diff -= ord('A')
                if c[diff] == 0: c[diff] = -1
                if c[diff] == 1:
                    c[diff] = 2
                    res +=1

            return res + dfs(i+1,c)

        return dfs(0,[0] * 26)
                