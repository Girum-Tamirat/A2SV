# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        gp = []
        lp = []
        pc = 0
        for num in nums:
            if num < pivot:
                lp.append(num)
            elif num > pivot:
                gp.append(num)
            if num == pivot:
                pc += 1
        nums.clear()
        for nu in lp:
            nums.append(nu)
        for _ in range(pc):
            nums.append(pivot)
        for nu in gp:
            nums.append(nu)
        return nums