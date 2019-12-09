from .linkedlist import LinkedList

class Queue(LinkedList):
    def __init__(self, items=None):
        super().__init__(items)
    
    def enqueue(self, data):
        self.append(data)

    def dequeue(self):
        if self.count == 0:
            self.delete()
        else: 
            self.delete(self.head.data)

class DoubleEndedQueue(LinkedList):
    def __init__(self, items=None):
        super().__init__(items)
    
    def enqueue_left(self, data):
        self.prepend(data)
    
    def enqueue_right(self, data):
        self.append(data)
    
    def dequeue_left(self):
        if self.count == 0:
            self.delete()
        else:
            self.delete(self.head.data)
    
    def dequeue_right(self):
        if self.count == 0:
            self.delete()
        else:
            self.delete(self.tail.data)

# if __name__ == "__main__":
    # q = Queue(['A', 'B', 'C'])
    # print(q)
    # q.enqueue('D')
    # print(q)
    # q.dequeue()
    # print(q)

    # dq = DoubleEndedQueue(['A', 'B', 'C'])
    # print(dq)
    # dq.enqueue_right('D')
    # print(dq)
    # dq.dequeue_left()
    # print(dq)
    # dq.enqueue_left('E')
    # print(dq)
    # dq.dequeue_right()
    # print(dq)