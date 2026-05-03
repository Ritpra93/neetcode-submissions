class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        rows, cols = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if node.isWord:
                res.add(word)
            visit.add((r, c))
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r+dr, c+dc
                if (0 <= nr < rows and 0 <= nc < cols and
                    (nr,nc) not in visit):
                    next_char = board[nr][nc]
                    if next_char in node.children:
                        dfs(nr, nc, node.children[next_char], word + next_char)
            visit.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                char = board[r][c]
                if char in root.children:
                    dfs(r, c, root.children[char], char)
        return list(res)


        