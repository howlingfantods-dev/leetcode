class Trie:
    def __init__(self):
        self.levels = []

    def insert(self, word): 
        for i in range(len(word)):
            if i + 1 >  len(self.levels):
                self.levels.append([0 for _ in range(26)])
            node = self.levels[i]
            char = word[len(word)-i-1]
            asc = ord(char) - ord('a')
            if node[asc] == 0:
                node[asc]+=1

    def lcs(word,query):
        L = len(self.levels) - 1
        qw = len(word) - 1
        for qi in range(len(query)-1,-1,-1):
            if qw == -1: break
            if query[qi] != word[qw]: break
            if self.levels[L][ord(query[qi]) - ord('a')] == 0: break
            qw-=1
        return len(word) - 1 - qw
            
            

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = [{}, -1, float('inf')] 

        def consider(node, length, idx):
            if length < node[2] or (length == node[2] and idx < node[1]):
                node[2], node[1] = length, idx

        for idx, w in enumerate(wordsContainer):
            consider(root, len(w), idx)
            node = root
            for ch in reversed(w):
                node = node[0].setdefault(ch, [{}, -1, float('inf')])
                consider(node, len(w), idx)

        res = []
        for q in wordsQuery:
            node = root
            for ch in reversed(q):
                if ch in node[0]:
                    node = node[0][ch]
                else:
                    break
            res.append(node[1])
        return res