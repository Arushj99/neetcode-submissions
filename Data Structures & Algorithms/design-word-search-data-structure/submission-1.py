class TrieNode():
    def __init__(self):
        self.children = {} #Key: Character, Value: TrieNode
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        found = [False]
        n = len(word)
        ''' Implement a dfs that if a character is '.' then I want to go down
        every path of characters available in the children dictionary. Base condition - if the letter is not in the child, 
        then return. If the last letter is in curr.children and and endOfWord = True, update search to True'''
        def dfs(curr, idx): 
            if idx == n:
                if curr.endOfWord:
                    found[0] = True
                return 
            if word[idx] == ".":
                for trie in curr.children.values():
                    dfs(trie, idx + 1)
            else:
                if word[idx] not in curr.children:
                    return 
                dfs(curr.children[word[idx]], idx + 1)
        dfs(self.root, 0)
        return found[0]
            

            
            
            
            

            
        
