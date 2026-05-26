class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        b = [0] * 26
        for c in string.ascii_lowercase:
            if c in word:    
                b[ord(c) - ord('a')] +=1

        for c in string.ascii_uppercase:
            if c in word:    
                b[ord(c) - ord('A')] +=1

        ans = 0 
        for i in b:
            if i == 2:
                ans+=1
        return ans