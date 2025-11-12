class LinkedListImplementation:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head):
        self.head = None

    def Insert(self, data):
        Node = LinkedListImplementation(data)
        if (self.head == None) :
            self.head = Node
            return
        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next
        currentNode.next = Node

    def Display(self):
        currentNode = self.head
        while currentNode :
            print(currentNode.data)
            currentNode = currentNode.next

    def Sort(self):
        if self.head is None or self.head.next is None:
            return
        
        swapped = True
        while swapped:
            swapped = False
            currentNode = self.head
            while currentNode.next:
                if currentNode.data > currentNode.next.data:
                    currentNode.data , currentNode.next.data = currentNode.next.data, currentNode.data
                    swapped = True
                currentNode = currentNode.next

    def Delete(self, data):
        if self.head is None:
            return

        if self.head.data == data :
            self.head = self.head.next

        currentNode = self.head
        previousNode = None
        while currentNode and currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.next

        if currentNode is None:
            print("The Value is not found.")
            return
        previousNode.next = currentNode.next


  
# Creating a linked list

l1 = LinkedList(10)

# Inserting elements to the Linked list

l1.Insert(15) 
l1.Insert(77) 
l1.Insert(12) 
l1.Insert(13) 
l1.Insert(16) 

# Deleting element from the Linked list

l1.Delete(16)

# Sorting elements of Linked List

l1.Sort()

# Displaying elements of Linked list

l1.Display()
