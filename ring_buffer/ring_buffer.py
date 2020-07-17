class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []
        self.counter = []


    def append(self, item):
        # if the length of the items is less than or equal to the self.capacity,
        # let the items in
        if len(self.items) < self.capacity:
            self.items.append(item)

        else:
            # len(self.items) == self.capacity:
            if self.counter == []:
                self.counter = 0
            if self.counter == self.capacity:
                self.counter = 0 
            self.items.pop(self.counter)
            self.items.insert(self.counter, item)
            self.counter += 1
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
