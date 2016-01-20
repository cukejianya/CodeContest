def insert(self,head,data):
    #Complete this method
        node = head
        if (!node):
            return Node(data)

        while(node.next):
            node = node.next
