class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            node=node.children[char]
        node.end=True

    def find_root(self,word):
        node = self.root
        root = ""
        for char in word:
            if char not in node.children:
                break  
            node = node.children[char]
            root += char
            if node.end:  
                return root
        return word  

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        
        for root in dictionary:
            trie.insert(root)

        words = sentence.split()  
        replaced_words = [trie.find_root(word) for word in words]

        return " ".join(replaced_words)
