class Node:
    def __init__(self, v, p, n):
        self.value = v
        self.prev = p
        self.next = n


class LinkList:

    def __init__(self):
        self.head = Node(0, None, None)

    def insert(self, value):
        node = self.head

        while node.next:
            node = node.next

        node.next = Node(value, node, None)

    def erase(self, value):
        node = self.head

        while node.next:
            if node.value == value:
                node.prev.next = node.next
                node.next.prev = node.prev
                del node
                return

            node = node.next
        print("not found target:", value)

    def traverse(self):
        node = self.head.next

        while node:
            print('cur-node: ', node.value)
            node = node.next


lk = LinkList()
lk.insert(3)
lk.insert(4)
lk.insert(5)
lk.insert(6)
lk.erase(4)
lk.traverse()
