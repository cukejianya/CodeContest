def insert(self,head,data):
#Complete this method
    node = head
    if not node:

        return Node(data)

    while(node.next):
        node = node.next
    node.next = Node(data)

    return head
