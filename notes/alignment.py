from sys import argv
# function from Marc feely
def createMatrix(numRow,numColumn):
    result = [None] * numRow
    for i in range(numRow):
        result[i] = [0]*numColumn
    return result

def alignement_global(A,B):
    lenA = len(A)
    lenB = len(B)
    #initialisation: lenA rows ,lenB cols
    T = createMatrix(lenA + 1, lenB + 1)
    T[0][0] = 0
    for i in range(lenA+1):
        T[i][0] = i
    for j in range(lenB+1):
        T[0][j] =j  
    #print B
    print("?    ",end = "")
    for i in range(1,lenB+1):
        print(B[i-1],end = "  ")
    print("")
    #firstrow
    print(" "+str(T[0]))
    #fill the table:
    for i in range(1,lenA+1):
        for j in range(1,lenB+1):
            left = T[i][j-1]
            diagonal = T[i-1][j-1]
            up = T[i-1][j]

            delta = 0 if (A[i-1] == B[j-1]) else 1

            T[i][j] = min(left+1, up+1, diagonal+delta);
        #print each row
        print(A[i-1]+str(T[i]))


def alignement_local(A,B):
    lenA = len(A)
    lenB = len(B)
    #initialisation: lenA rows ,lenB cols
    T = createMatrix(lenA + 1, lenB + 1)
    T[0][0] = 0
    for i in range(lenA+1):
        T[i][0] = i
    for j in range(lenB+1):
        T[0][j] =j  
    #print B
    print("?    ",end = "")
    for i in range(1,lenB+1):
        print(B[i-1],end = "  ")
    print("")
    #firstrow
    print(" "+str(T[0]))
    #fill the table:
    for i in range(1,lenA+1):
        for j in range(1,lenB+1):
            left = T[i][j-1]
            diagonal = T[i-1][j-1]
            up = T[i-1][j]

            delta = 0 if (A[i-1] == B[j-1]) else 1

            T[i][j] = min(left+1, up+1, diagonal+delta);
        #print each row
        print(A[i-1]+str(T[i]))

alignement_global(argv[1],argv[2])
        


