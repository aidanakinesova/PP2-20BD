class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        for i in str(n):
            product *= int(i)
            sum += int(i)
        return(product - sum)