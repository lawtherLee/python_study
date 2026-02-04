class SingleLinkList(object):
    def __init__(self, node=None):
        self.head = node

    def is_empty(self):
        return self.head is None

    def length(self):
        """链表长度"""
        count = 0
        cur = self.head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.head
        while cur is not None:
            print(cur.item)
            cur = cur.next
