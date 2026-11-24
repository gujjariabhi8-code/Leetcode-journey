class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sm = 0
        dup_x = x
        while(dup_x > 0):
            sm += dup_x % 10
            dup_x = dup_x // 10
        if x % sm == 0:
            return sm
        return -1