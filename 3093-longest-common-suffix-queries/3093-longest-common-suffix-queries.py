class Node:
    def __init__(self):
        self.children = {}
        self.idx = -1
        self.length = inf

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:

        root = Node()
        def make(node,idx,length):
            if (length < node.length
                or (length == node.length and idx < node.idx)):
                node.length = length
                node.idx = idx

        for i, w in enumerate(wordsContainer):
            make(root, i, len(w))
            node = root
            for ch in reversed(w):
                if ch not in node.children:
                    node.children[ch] = Node()
                node = node.children[ch]
                make(node,i, len(w))

        res = []

        for q in wordsQuery:
            node = root
            for ch in reversed(q):
                if ch in node.children:
                    node = node.children[ch]
                else: break
            res.append(node.idx)

        return res














