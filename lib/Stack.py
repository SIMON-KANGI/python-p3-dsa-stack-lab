class Stack:
    
    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit
        
        pass

    def isEmpty(self):
        return len(self.items) == 0
            

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        
        

    def pop(self):
        pass

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)
        

    def full(self):
        return len(self.items) == self.limit
            

    def search(self, target):
        distance = 0
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == target:
                return distance
            else:
                distance += 1
        return -1

