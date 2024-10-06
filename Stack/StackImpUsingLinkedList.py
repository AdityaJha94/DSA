class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self,item):
        newNode = Node(item)
        if self.top == None:
            self.top = newNode
            return
        currentTop = self.top
        self.top = newNode
        self.top.next = currentTop

    def pop(self):
        if self.top == None:
            return
        if self.top.next == None:
            self.top = None
            return
        currentSecond = self.top.next
        del self.top
        self.top = currentSecond

    def peek(self):
        return self.top.value

    
    def printValues(self):
        current = self.top
        while current is not None:
            print(current.value)
            current = current.next

s = Stack()
s.push(1)
s.push(5)
s.push(6)
s.push(2)
s.push(9)
s.push(7)
s.pop()
s.pop()
s.pop()
s.push(11)
s.printValues()
print(s.peek())
        
