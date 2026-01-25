class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        sol=[[0]*len(board[0]) for i in range(len(board))]
        def bt(x,y,i=0):

            if x<0 or x>=len(board):
                return False
            if y<0 or y>=len(board[0]):
                return False
            if sol[x][y]!=0:
                return False
            if word[i]!=board[x][y]:
                return False

            if i==len(word)-1:
                return True
            sol[x][y]=1
            if (bt(x+1,y,i+1) or
             bt(x,y+1,i+1) or
             bt(x,y-1,i+1) or
             bt(x-1,y,i+1)) :
                return True
            sol[x][y]=0
            return False
        for j in range(len(board[0])):
            for k in range(len(board)):
                if bt(k,j):
                    return True
        return False



