from singlenode import *
from singleLinkList import *

if __name__ == "__main__":
    sn1 = SingleNode("苗人凤")

    print(f"sn1节点:\t{sn1}")
    print(f"sn1节点的下一个节点:\t{sn1.next}")

    ll = SingleLinkList(sn1)
    print(f"链表头节点:\t{ll.head}")
    print(f"链表是否为空:\t{ll.is_empty()}")
    print(f"链表长度:\t{ll.length()}")

    ll.travel()
