# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.map = {}  # Stores value -> index mapping
        self.list = []  # Stores values for O(1) getRandom

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False  # Value already exists
        self.map[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False  # Value doesn't exist
        
        index = self.map[val]
        last_element = self.list[-1]

        # Swap the element to remove with the last element
        self.list[index] = last_element
        self.map[last_element] = index

        # Remove the last element
        self.list.pop()
        del self.map[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()