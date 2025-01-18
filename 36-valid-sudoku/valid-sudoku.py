class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        checkrow=defaultdict(set)
        checkcol=defaultdict(set)
        checkmat=defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                if (board[r][c] in checkrow[r] or 
                board[r][c] in checkcol[c] or 
                board[r][c] in checkmat[(r//3,c//3)]):
                    return False
                
                checkcol[c].add(board[r][c])
                checkrow[r].add(board[r][c])
                checkmat[(r//3,c//3)].add(board[r][c])
            
        return True

