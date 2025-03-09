# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        m = 0
        for i in range(len(processorTime)):
            m = max(m, processorTime[i] + tasks[i * 4])
        return m