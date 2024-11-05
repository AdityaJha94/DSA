import sys
class KStacks:
    def __init__(self,cap,k):
        self.arr = [None]*cap
        self.free_top = 0
        self.topArr = [-1]*k
        self.next = [i+1 for i in range(cap-1)]
        self.next.insert(cap-1,-1)
        print(self.next)

    def push(self,sn,item) -> bool:
        if self.isFull():
            return False
        i = self.free_top
        self.free_top = self.next[i]
        self.next[i] = self.topArr[sn]
        self.topArr[sn] = i
        self.arr[i] = item
        return True

    def pop(self,sn) -> int:
        if self.isEmpty(sn):
            return sys.maxsize-1
        i = self.topArr[sn]
        self.topArr[sn] = self.next[i]
        self.next[i] = self.free_top
        self.free_top = i
        item =  self.arr[i]
        self.arr[i] = None
        return item
        
    def isEmpty(self,sn) -> bool:
        return self.topArr[sn] == -1

    def isFull(self) -> bool:
        return self.free_top == -1

    def printStack(self):
        print(self.arr)

stack = KStacks(10,5)
stack.push(1,100)
stack.push(1,200)
stack.push(3,400)
stack.push(2,500)
stack.push(4,600)
stack.pop(1)
stack.printStack()
