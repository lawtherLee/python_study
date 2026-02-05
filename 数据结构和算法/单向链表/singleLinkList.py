from singlenode import SingleNode


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
            print(f"\t\t\t{cur.item}")
            cur = cur.next

    def add(self, item):
        """链表头部添加元素"""
        new_node = SingleNode(item)
        new_node.next = self.head
        self.head = new_node

    def append(self, item):
        """链表尾部添加元素"""
        new_node = SingleNode(item)
        if self.is_empty():
            self.head = new_node
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def insert(self, pos, item):
        """
        往指定位置添加
        :param pos: 要添加到的索引
        :param item: 要添加的元素
        :return: None
        """
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            cur = self.head
            count = 0
            while count < pos - 1:
                count += 1
                cur = cur.next
            new_node = SingleNode(item)
            new_node.next = cur.next
            cur.next = new_node

    def remove(self, item):
        """删除节点"""
        cur = self.head
        pre = None
        while cur is not None:
            if cur.item == item:
                if pre is None:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False
