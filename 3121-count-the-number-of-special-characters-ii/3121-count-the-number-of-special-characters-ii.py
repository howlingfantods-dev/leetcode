class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        for ch,CH in zip(string.ascii_lowercase,string.ascii_uppercase):
            if ch in word and CH in word: 
                ans += word.rfind(ch) < word.find(CH)
        return ans