class Stack:
    stack=[]
    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit
        
        pass

    def isEmpty(self):
        if len(self.items) == 0:
            return None

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
        pass

    def search(self, target):
        return self.items[target]
        
