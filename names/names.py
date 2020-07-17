import time
from collections import deque


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

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

#  filler = []
# # while len(names_1):
#     # filler.append(names_1.pop())
#     # filler.append(names_2.pop())
#     # filler.sort()
# names_1.sort()
# names_2.sort()


def sortnapp(lis):
    while len(lis):
        n1 = lis.pop()
        if len(lis) > 1:
            if n1 == lis[-1]:
                None
            else:
                filler.append(n1)


sortnapp(names_1)
sortnapp(names_2)
filler.sort()

while len(filler):
    current = filler.pop()
    if len(filler) > 1:
        last = filler[-1]

        print(last)
        if str(current) == str(last):
            duplicates.append(current)






####################
# for name2 in names_2:
#     while len(names_1) > 0:
#         current = names_1.pop()
#         if current == name2:
#             duplicates.append(current)
######################
# filler = []
# for name1 in names_1:
#     filler.append(name1)
#     while len(filler) > 0:
#         current = filler.pop()
#         for name2 in names_2:
#             if name2 == current:
#                 duplicates.append(current)
#             else:
#                 None
########################
# while len(names_1) > 0:
#     n1 = names_1.pop()
#     for n2 in names_2:
#         if n1 == n2:
#             duplicates.append(n1)
# names_1.extend(names_2)
####################
# Replace the nested for loops below with your improvements
################
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
