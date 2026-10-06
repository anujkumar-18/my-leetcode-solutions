# class Solution:
#     def fib(self, n: int) -> int:
#         if n <= 1:
#             return n
#         return self.fib(n - 1) + self.fib(n - 2)
class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def helper(k: int) -> int:
            if k <= 1:
                return k
            if k in memo:
                return memo[k]
            memo[k] = helper(k - 1) + helper(k - 2)
            return memo[k]

        return helper(n)