class Solution:
    def confusingNumber(self, n: int) -> bool:
        same = []
        rotate = 0 
        m = n 
        while m > 0:
            curr = m % 10
            print(curr)
            if curr not in [0,1,8,6,9]: return False
            if curr == 0: rotate = rotate * 10
            if curr == 6: rotate = rotate * 10 + 9
            if curr == 9: rotate = rotate * 10 + 6
            if curr == 1: rotate = rotate * 10 + 1
            if curr == 8: rotate = rotate * 10 + 8
            m//=10
        return rotate != n
