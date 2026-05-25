class Solution:
    def passwordStrength(self, password: str) -> int:
        seen = set()        
        ans = 0
        for p in password:
            if p not in seen:
                if p.isalpha() and p.islower():
                    ans +=1
                elif p.isalpha() and p.isupper():
                    ans +=2
                elif p.isdigit():
                    ans +=3
                elif p in "!@#$":
                    ans +=5
                seen.add(p)            

        return ans
