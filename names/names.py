import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare the input value with the value of the node
        # if value < Node 's Value
        if value < self.value:
            # we need to go left
            if self.left is None:
            # if there is no left child, then we can wrap the value
            #  in a BSTNode and park it
                self.left = BSTNode(value)
            else:
            # otherwise there is a child
            # call the left child's `insert` method
                self.left.insert(value)

        # otherwise, value > = Node's value
        else:
            # we need to go right
            if self.right is None:
            # if there is right child, then we can wrap the value
            #  in a BSTNode and park it 
                self.right = BSTNode(value)
            # call the right child's `insert` method
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        return self._search(target, self)

    def _search(self, target, currentNode):
        # if the current node is the target
        if target == currentNode.value:
            # return True
            return True
            # else if the target is less then the current node and there is a left node
        elif target < currentNode.value and currentNode.left is not None:
            # return this search on the target and left Node
            return self._search(target, currentNode.left)
            # else if the target is more then the current node and there is a right node
        elif target > currentNode.value and currentNode.right is not None:
            # return this search on the target and right Node
            return self._search(target, currentNode.right)


for n1 in names_1:
    BSTNode.insert(n1)
for n2 in names_2:
    BSTNode.insert(n2)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
