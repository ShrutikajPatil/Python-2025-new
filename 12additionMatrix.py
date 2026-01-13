A=[[1,2],[3,4]]
B=[[5,6],[7,8]]
C=[[0,0],[0,0]]
m=2

for i in range(m):
    for j in range(m):
        C[i][j]=A[i][j]+B[i][j]



print(C)        