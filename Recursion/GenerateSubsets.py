def generateSubsets(inputStr, curr = "", i = 0):
    if len(curr) == 0:
        print("empty string")
    else:
        print(curr)
    print(i)
    print("=================End of call====================")
    if i == len(inputStr):
        #print(curr)
        return
    generateSubsets(inputStr,curr,i+1)
    generateSubsets(inputStr,curr + inputStr[i], i+1)


resultSubset = []
def allSubsets(s,curr = "", i = 0):
    if i == len(s):
        if curr not in resultSubset:
            resultSubset.append(curr)
            return   
        
    if i < len(s):
        allSubsets(s,curr,i+1)
        allSubsets(s,curr+s[i],i+1)

def powerSet(s):
    allSubsets(s)
    return resultSubset

#result = generateSubsets("ABC")

powerSetResults = powerSet("ab")
print(powerSetResults)
