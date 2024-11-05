import Foundation

var arr = Array<Int>(repeating: Int.max, count: 10)
print(arr)
arr[1] = 1
print(arr)
class KStacks {
    private var arr: [Int]
    private var freeTop: Int
    private var topArr: [Int]
    private var next: [Int]
    
    init(cap: Int, k: Int) {
        self.arr = Array(repeating: Int.max, count: cap)
        self.freeTop = 0
        self.topArr = Array(repeating: -1, count: k)
        self.next = Array(0..<cap - 1) + [-1]
    }

    func push(_ sn: Int, item: Int) -> Bool {
        if isFull() {
            return false
        }
        
        let i = freeTop
        freeTop = next[i]
        next[i] = topArr[sn]
        topArr[sn] = i
        arr[i] = item
        
        return true
    }

    func pop(_ sn: Int) -> Int {
        if isEmpty(sn) {
            return Int.max // Using max value for empty stack
        }
        
        let i = topArr[sn]
        topArr[sn] = next[i]
        next[i] = freeTop
        freeTop = i
        let item = arr[i]
        arr[i] = Int.max // Clear the popped item
        return item // Return the item or max if nil
    }

    func isEmpty(_ sn: Int) -> Bool {
        return topArr[sn] == -1
    }

    func isFull() -> Bool {
        return freeTop == -1
    }

    func printStack() {
        print(arr)
    }
}

// Example usage:
let stack = KStacks(cap: 10, k: 5)
stack.push(1, item: 100)
stack.push(1, item: 200)
stack.push(3, item: 400)
stack.push(2, item: 500)
stack.push(4, item: 600)
stack.pop(1)
stack.printStack()
