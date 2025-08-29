# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        em = {e.id: e for e in employees}
        def dfs(eid):
            emp = em[eid]
            total = emp.importance
            for si in emp.subordinates:
                total += dfs(si)
            return total
        return dfs(id)