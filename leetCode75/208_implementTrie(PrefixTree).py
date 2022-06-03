""""

"""



class TrieNode:
    def __init__(self) -> None:
        self.children={}     # children["a"]=TrieNode()
        self.endOfWord=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        cur=self.root
        for c in word:
            # character does not currently exist in the children then we add it and then create an empty node to it
            if c not in cur.children:
                cur.children[c]=TrieNode()
            # advance cur to point at the character we previously added
            cur=cur.children[c]
        # we are done adding the current word then we have to make it the end of the word 
        cur.endOfWord=True

    def search(self, word: str) -> bool:
        cur=self.root
        for c in word:
            if c not in cur.children:
                return False
            cur=cur.children[c]
         # when we reach the end we just return the state in endOfWord of what currently is in the currennt node we a looking at
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for c in word:
            if c not in cur.children:
                return False
            cur=cur.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)