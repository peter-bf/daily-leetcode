import time

# Needs work, need to pregenerate all possible palindromes in base 10, then convert to base k and check if it's a palindrome

class Solution:
    def to_base(self, n, b):
        # print(f"converting {n} to base {b}")
        if n == 0:
            return "0"
        res = ""
        while n:
            res = str(n % b) + res
            n //= b
        return res

    def is_palindrome(self, s):
        return s == s[::-1]

    def kMirror(self, k: int, n: int) -> int:
        mirrors = []
        num = 1
        start_time = time.time()
        while len(mirrors) < n:
            base_k = self.to_base(num, k)
            if self.is_palindrome(str(num)) and self.is_palindrome(base_k):
                print(f"found mirror {num}, {len(mirrors)}/{n}")
                mirrors.append(num)
            num += 1
        end_time = time.time()
        print(f"\ntime taken: {end_time - start_time} seconds")
        print(mirrors)
        return sum(mirrors)
    
sol = Solution()
sol.kMirror(7, 17)