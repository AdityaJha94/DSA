# Time Complexity: O(N + M).

def KMPPatternSearch(txt,pat):
    if len(pat) == 0:
        return 0
    # Create the LPS table now
    lps = [0]*len(pat)
    prevLPS,i = 0,1
    while i < len(pat):
        if pat[i] == pat[prevLPS]:
            lps[i] = prevLPS+1
            prevLPS += 1
            i += 1
        elif prevLPS == 0:
            lps[i] = 0
            i += 1
        else:
            prevLPS = lps[prevLPS-1]

    # Use LPS now for pattern searching
    i = 0
    j = 0
    while i < len(txt):
        if txt[i] == pat[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j-1]
        if j == len(pat):
            return i - len(pat)
    return -1

txt = 'AAAXAAAA'
pat = 'AAAA'
result = KMPPatternSearch(txt,pat)
print(result)
        
