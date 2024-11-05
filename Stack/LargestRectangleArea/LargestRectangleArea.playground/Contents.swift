func largestRectangleArea(_ heights: [Int]) -> Int {
    var maxArea = 0
    var stack: [(index: Int, height: Int)] = []
    
    for (i, h) in heights.enumerated() {
        var start = i
        
        while let last = stack.last, last.height > h {
            let (index, height) = stack.removeLast()
            maxArea = max(maxArea, height * (i - index))
            start = index
        }
        
        stack.append((start, h))
    }
    
    for (i, h) in stack {
        maxArea = max(maxArea, h * (heights.count - i))
    }
    
    return maxArea
}

let heights = [2, 1, 5, 6, 2, 3]
let result = largestRectangleArea(heights)
print(result)
