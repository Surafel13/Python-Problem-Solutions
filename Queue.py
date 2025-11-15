class Queue:
    def __init__(self):
        self.queue = []

    def Enqueue(self, data):
        self.queue.append(data)
        return

    def Display (self):
        if len(self.queue) == 0:
            print("Queue is empty.")
        else :
            for i in self.queue:
                print(i)
    
    def Dequeue (self) : 
        if len(self.queue) == 0:
            print("Queue is empty")

        else :
            self.queue.pop(0)

    def Peek(self) :
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print(self.queue[0])





l1 = Queue()

l1.Enqueue(2)
l1.Enqueue(3)
l1.Enqueue(5)
l1.Enqueue(6)

l1.Dequeue()


l1.Display()


