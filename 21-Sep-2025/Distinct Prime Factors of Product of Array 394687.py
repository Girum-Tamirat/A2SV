# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        f = []
        for num in nums:
            while num%2==0:
                f.append(2)
                num//=2
            for i in range(3, int(num**0.5)+1, 2):
                while num%i==0:
                    f.append(i)
                    num//=i
            if num>2: f.append(num)
        c = Counter(f)
        return len(c)