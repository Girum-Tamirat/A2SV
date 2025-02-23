# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

class FrequencyTracker:
    def __init__(self):
        self.a = {}
        self.b = {}

    def add(self, x: int) -> None:
        if x in self.a:
            y = self.a[x]
            self.b[y] -= 1
            if self.b[y] == 0:
                del self.b[y]
            self.a[x] += 1
        else:
            self.a[x] = 1
        z = self.a[x]
        self.b[z] = self.b.get(z, 0) + 1

    def deleteOne(self, x: int) -> None:
        if x in self.a:
            y = self.a[x]
            self.b[y] -= 1
            if self.b[y] == 0:
                del self.b[y]
            
            if y > 1:
                self.a[x] -= 1
                z = self.a[x]
                self.b[z] = self.b.get(z, 0) + 1
            else:
                del self.a[x]

    def hasFrequency(self, f: int) -> bool:
        return self.b.get(f, 0) > 0

# Example Usage:
# obj = FrequencyTracker()
# obj.add(3)
# obj.add(3)
# print(obj.hasFrequency(2))  # True
# obj.deleteOne(3)
# print(obj.hasFrequency(2))  # False
