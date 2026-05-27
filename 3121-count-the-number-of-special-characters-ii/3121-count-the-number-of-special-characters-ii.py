class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c = [0] * 26
        n = len(word)
        ans = 0
        for i in range(n):
            diff = ord(word[i]) 
            if word[i].islower():
                diff -= ord('a')
                if c[diff] == 0: c[diff]+=1
                if c[diff] == 2:
                    ans-=1
                    c[diff]= -1

            if word[i].isupper():
                diff -= ord('A')
                if c[diff] == 0: c[diff] = -1
                if c[diff] != 1: continue
                c[diff] = 2
                ans +=1
        return ans

                