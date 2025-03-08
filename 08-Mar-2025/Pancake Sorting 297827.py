# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(arr, k):
            arr[:k] = reversed(arr[:k]) 
        result = []
        for size in range(len(arr), 0, -1):
            mi = arr.index(size)  
            if mi == size - 1:
                continue  
            if mi != 0:
                result.append(mi + 1)  
                flip(arr, mi + 1)
            result.append(size)
            flip(arr, size)
        return result