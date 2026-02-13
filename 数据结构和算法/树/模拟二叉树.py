class Node:
    def __init__(self, item):
        self.item = item
        self.l_child = None
        self.r_child = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def add(self, item):
        if self.root is None:
            self.root = Node(item)
            return

        queue = [self.root]

        while True:
            root_node = queue.pop(0)
            if root_node.l_child is None:
                root_node.l_child = Node(item)
                return
            elif root_node.r_child is None:
                root_node.r_child = Node(item)
                return
            else:
                queue.append(root_node.l_child)
                queue.append(root_node.r_child)

    def breadth_travel(self):
        """广度优先遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.item, end=" ")
            if node.l_child is not None:
                queue.append(node.l_child)
            if node.r_child is not None:
                queue.append(node.r_child)

    def preorder_travel(self, root):
        """深度优先遍历(前序遍历:根左右)"""
        if root is not None:
            print(root.item, end=" ")
            self.preorder_travel(root.l_child)
            self.preorder_travel(root.r_child)
        # 非递归实现
        # if self.root is None:
        #     return
        # stack = [self.root]
        # while stack:
        #     node = stack.pop()
        #     print(node.item, end=" ")
        #     if node.r_child is not None:
        #         stack.append(node.r_child)
        #     if node.l_child is not None:
        #         stack.append(node.l_child)

    def inorder_travel(self, root):
        """深度优先遍历(中序遍历:左根右)"""
        if root is not None:
            self.preorder_travel(root.l_child)
            print(root.item, end=" ")
            self.preorder_travel(root.r_child)

    def postorder_travel(self, root):
        """深度优先遍历(后序遍历:左右根)"""
        if root is not None:
            self.preorder_travel(root.l_child)
            self.preorder_travel(root.r_child)
            print(root.item, end=" ")


def demo():
    node = Node("泰温")

    # print(f"节点的内容:{node.item}")
    # print(f"节点的左子树:{node.l_child}")
    # print(f"节点的右子树:{node.r_child}")

    bt = BinaryTree(node)
    bt.add("詹姆")
    bt.add("瑟曦")

    print("广度优先遍历")
    bt.breadth_travel()
    print("\n")

    print("深度优先遍历")
    bt.preorder_travel(bt.root)
    print("\n")

    bt.inorder_travel(bt.root)
    print("\n")

    bt.postorder_travel(bt.root)
    # print(f"二叉树:{bt}")
    # print(f"二叉树的根节点:{bt.root.item}")


if __name__ == "__main__":
    demo()
