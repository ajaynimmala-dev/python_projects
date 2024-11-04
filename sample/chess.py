def isvalid(board,i,j,N):
    for k in range(j):
        if board[i][k]==1:
            return False
    for k,l in zip(range(i,-1,-1),range(j,-1,-1)):
        if board[k][l]==1:
            return False
    for k,l in zip(range(i,N,1),range(j,N,-1)):
        if board[k][l]==1:
            return False
    return True

def solve(board,col,N):
    if col==N:
        return True
    else:
        for i in range(N):
            if(isvalid(board,i,col,N)):
                board[i][col]=1
                if(solve(board,col+1,N)):
                    return True
                board[i][col]=0
    return False

N=int(input("enter N\t"))
board=[]
board=[[0 for i in range(N)]for k in range(N)]
res=solve(board,0,N)
print(board)
if res == True:
    for i in board:
        print(i)


