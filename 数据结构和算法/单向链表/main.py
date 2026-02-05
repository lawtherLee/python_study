from singleLinkList import *

if __name__ == "__main__":
    sn1 = SingleNode("苗人凤")

    ll = SingleLinkList(sn1)

    ll.add("胡一刀")
    ll.append("马春花")
    ll.insert(1, "王小虎")
    ll.remove("王小虎")

    print(f"链表头节点:\t{ll.head.item}")
    print(f"链表是否为空:\t{ll.is_empty()}")
    print(f"链表长度:\t{ll.length()}")
    print("-" * 100)

    print("链表内容:")
    ll.travel()
