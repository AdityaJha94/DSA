from sys import maxsize 
class Stack:
    values = []
    def __init__(self):
        pass

    def push(self,item):
        self.values.append(item)

    def pop(self):
        if self.isEmpty():
            return str(-maxsize-1) # return minus infinite

        self.values.pop()
            

    def peek(self) -> int:
        if self.isEmpty():
            return str(-maxsize-1) # return minus infinite

        return self.values[len(self.values)-1]

    def isEmpty(self) -> bool:
        return len(self.values) == 0

s = Stack()
s.push(1)
s.push(5)
s.push(6)
s.push(2)
s.push(9)
s.push(7)
s.pop()
s.push(5)
s.pop()
s.pop()
print(s.values)
print(s.peek())
