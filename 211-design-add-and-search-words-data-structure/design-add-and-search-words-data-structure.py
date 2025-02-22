class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            node=node.children[char]
        node.end=True
        
    def searchHelp(self,node,word,index):
        if index==len(word):
            return node.end

        char=word[index]
        if char == '.':
            for child in node.children.values():
                if self.searchHelp(child,word,index+1):
                    return True

            return False

        if char not in node.children:
            return False

        return self.searchHelp(node.children[char],word,index+1)


    def search(self, word: str) -> bool:
        return self.searchHelp(self.root, word, 0) 
        
