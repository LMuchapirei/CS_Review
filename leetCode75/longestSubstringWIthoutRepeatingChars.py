



def lengthOfLongestSubstring(s):
    l=0
    charSet=set()
    res=0
    for r in range(len(s)):
        currChar=s[r]
        while currChar in charSet:
            charSet.remove(currChar)
            l+=1
        charSet.add(currChar)
        res=max(res,r-l+1)
    return res



print(lengthOfLongestSubstring("abcabcbb"))