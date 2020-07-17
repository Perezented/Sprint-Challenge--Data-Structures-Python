class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def append(self, item):
        # if the length of the items is less than or equal to the self.capacity,
        # let the items in
        counter = 0
        if len(self.items) < self.capacity:
            self.items.insert(self.capacity, item)
        if len(self.items) == self.capacity:
            self.items.insert(counter, item)
            self.items.pop()
            counter += 1
            if counter == self.capacity:
                counter = 0

        # else if the lenght is the self.capacity, have it insert to 0 up to the self.capacity

    # return all items in the ring buffer list
    def get(self):
        return self.items
