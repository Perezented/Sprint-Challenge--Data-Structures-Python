class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def append(self, item):
        self.items.insert(self.capacity, item)

    def get(self):
        return self.items
