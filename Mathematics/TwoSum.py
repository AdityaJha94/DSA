def twoSum(nums, target):
    tempDict = {}
    for i in range(len(nums)):
        tempDict[nums[i]] = i
    print(tempDict)
    for i in range(len(nums)):
        requiredValue = target - nums[i]
        print("requiredValue: {}".format(requiredValue))
        if requiredValue in tempDict:
            return [i, tempDict[requiredValue]]
    return []
nums = [3,2,4]
result = twoSum(nums,6)
print(result)
