class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class QueueImpUsingLinkedList:
    def __init__(self):
        self.top = None
        self.current = None
    

    def enqueue(self,item):
        newNode = Node(item)
        if self.top == None:
            self.top = newNode
            self.current = newNode
            return
        self.current.next = newNode
        self.current = newNode

    def dequeue(self):
        if self.top is None:
            return
        nextTop = self.top.next
        del self.top
        self.top = nextTop

    def getFront(self):
        return self.top.value
        

    def getRear(self):
        return self.current.value

    def printValues(self):
        currentNode = self.top
        while currentNode is not None:
            print(currentNode.value)
            currentNode = currentNode.next

queue = QueueImpUsingLinkedList()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.printValues()
queue.dequeue()
queue.dequeue()
queue.printValues()
print('front:- ', queue.getFront())
print('rear:- ', queue.getRear())

        
