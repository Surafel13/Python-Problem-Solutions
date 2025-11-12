class StackClasse:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def isEmpty(self):
        if(len(self.stack) == 0):
            return True
        else :
            return False

    def pop(self):
        if(len(self.stack) == 0):
            return ("The stack is empty.")
        else:
            self.stack.pop()
    
    def iterator(self):
        if(len(self.stack) == 0):
            return ("The stack is empty.")
        else:
            for i in range(len(self.stack)):
                print(self.stack[i])



myStack = StackClasse()

print(myStack.isEmpty())

myStack.push(2)
myStack.push(4)
myStack.push(6)

myStack.iterator()

myStack.pop()
myStack.iterator()


