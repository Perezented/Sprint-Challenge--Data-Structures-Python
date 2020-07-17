class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # if there is no node, just return 
        if node is None:
            return
        # set up prev to none and current to self.head
        prev = None
        current = self.head
        nex = current.get_next()
        # while current is true
        while current:
            # set the next to prev
            current.set_next(prev)
            # the next item, now prev item
            prev = current
            # set the next item of prev as current
            current = nex
            # if next is still possible, set next to get next
            if nex:
                nex = nex.get_next()
        # finally have head set as the final prev
        self.head = prev

        # if node is None:
        #     return
        # current = self.head
        # while current:
        #     if current.get_value():
        #         print(current.get_value())
        #     if current.get_next():
        #         current = current.get_next()
        #     else:
        #         break
            
