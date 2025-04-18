# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        nn = ListNode(val)
        nn.next = self.head
        self.head = nn
        self.size += 1

    def addAtTail(self, val: int) -> None:
        nn = ListNode(val)
        if not self.head:
            self.head = nn
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = nn
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        cur = self.head
        for _ in range(index - 1):
            cur = cur.next
        nn = ListNode(val)
        nn.next = cur.next
        cur.next = nn
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        cur = self.head
        for _ in range(index - 1):
            cur = cur.next
        if cur.next:
            cur.next = cur.next.next
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)