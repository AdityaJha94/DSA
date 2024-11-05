class TwoStacks:
    cap,top1,top2 = 0,0,-1
    def __init__(self,cap,top1,top2):
        self.cap = cap
        self.top1 = top1
        self.top2 = top2
        self.arr = [None]*cap

    def push1(self,item: int) -> bool:
        print("PUSH top1 before:- {}".format(self.top1))
        if self.top1 < self.top2-1:
            self.top1 += 1
            self.arr[self.top1] = item
            print("PUSH top1 after:- {}".format(self.top1))
            print(self.arr)
            print("=================================================")

    def push2(self,item: int) -> bool:
        print("PUSH top2 before:- {}".format(self.top2))
        if self.top1 < self.top2-1:
            self.top2 -= 1
            self.arr[self.top2] = item
            print("PUSH top2 before:- {}".format(self.top2))
            print(self.arr)
            print("=================================================")

    def pop1(self) -> int:
        print("POP top1 before:- {}".format(self.top1))
        if self. arr and self.top1 >= 0:
            self.arr[self.top1] = None
            self.top1 -= 1
            print("POP top1 after:- {}".format(self.top1))
            print(self.arr)
            print("=================================================")

    def pop2(self) -> int:
        print("POP top2 before:- {}".format(self.top2))
        if self.arr and self.top2 < self.cap:
            self.arr[self.top2] = None
            self.top2 += 1
            print("POP top2 after:- {}".format(self.top2))
            print(self.arr)
            print("=================================================")

    def size1(self) -> int:
        return self.top1+1

    def size2(self) -> int:
        return self.cap-self.top2

twoStack = TwoStacks(10,-1,10)
twoStack.push1(1)
twoStack.push1(2)
twoStack.push1(5)
twoStack.push1(6)
twoStack.push1(3)
twoStack.push1(8)
twoStack.push2(1)
twoStack.push2(20)
twoStack.push2(25)
twoStack.pop1()
twoStack.pop2()
twoStack.pop2()
twoStack.pop2()
twoStack.pop2()
twoStack.pop2()
twoStack.pop1()
twoStack.pop1()
twoStack.pop1()
twoStack.pop1()
twoStack.pop1()
twoStack.pop1()
twoStack.pop1()
twoStack.pop1()
twoStack.pop1()
print(twoStack.size1())
print(twoStack.size2())


    

    
