# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights)-1):
            d = heights[i+1]-heights[i]
            if d > 0:
                bricks -= d
                heappush(heap, -d)
                if bricks<0 and ladders>0:
                    s = -heappop(heap)
                    ladders-=1
                    bricks+=s
                if bricks<0 and ladders==0:
                    return i
        return len(heights)-1