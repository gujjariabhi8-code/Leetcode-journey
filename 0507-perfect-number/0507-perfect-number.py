class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        sm = 1
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                if i*i == num:
                    sm += i
                else:
                    sm += (i + num/i)
        return sm == num
                


