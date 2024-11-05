class QueueImpUsingArray:
    def __init__(self):
        self.arr = []

    def enqueue(self, item: int):
        self.arr.append(item)

    def dequeue(self) -> int:
        if not self.isEmpty():
            del self.arr[0]

    def isEmpty(self) -> bool:
        return len(self.arr) == 0

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.arr[0]
        return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.arr[len(self.arr)-1]

    def printQueue(self):
        print(self.arr)

queue = QueueImpUsingArray()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.printQueue()

queue.dequeue()
queue.dequeue()
queue.printQueue()
print('front:- ', queue.getFront())
print('rear:- ', queue.getRear())
