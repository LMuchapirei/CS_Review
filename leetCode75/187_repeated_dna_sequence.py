"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.
Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.
"""

"""Idea is to find all the nth sized substring in the given string s
   add them to a hashset and when they apear then add them to the list of results

   Key questions is how do you find all the substrings in a given string
   How to create a hashset and then add elements to it
"""


class Solution:
    def findRepeatedDnaSequences(self,s):
        seen,res=set(),set()

        size=len(s)-9
        for l in range(size):
            cur=s[l:l+10]
            if cur in seen:
                res.add(cur)
            seen.add(cur)

        return list(res)

    def findRepeatedDnaSequencesT(self,s):
        substr=self.makeSubstrings(s,10)
        seen=set()
        for i in substr:
            seen.add(i)   
        return list(seen)

    def makeSubstrings(self,s,sblen):
        substrings=[]
        size=len(s)-sblen-1
        for l in range(size):
            cur=s[l:l+sblen]
            substrings.append(cur)
        return substrings

test=Solution()

print(test.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(test.findRepeatedDnaSequencesT("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))

