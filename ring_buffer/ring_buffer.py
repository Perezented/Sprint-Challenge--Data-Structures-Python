class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def append(self, item):
        # if the length of the items is less than or equal to the self.capacity,
        # let the items in
        counter = -self.capacity
        if len(self.items) < self.capacity:
            self.items.insert(self.capacity - 1, item)
        elif len(self.items) == self.capacity:
            counter += 1
            self.items.pop(counter)
            self.items.insert(0, item)
            # if counter == self.capacity:
            #     counter = 0
        
        # if len(self.items) == self.capacity:
        #     self.items.insert(counter, item)
        #     # print(self.items)
        #     print(counter)
        #     # self.items.pop(0)
        #     counter -= 1
        #     if counter == 0:
        #         counter = self.capacity

        # else if the lenght is the self.capacity, have it insert to 0 up to the self.capacity

    # return all items in the ring buffer list
    def get(self):
        return self.items
