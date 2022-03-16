import time
import sys

# function from Marc feely
def createMatrix(numRow,numColumn):
    result = [None] * numRow
    for i in range(numRow):
        result[i] = [0]*numColumn
    return result


# 1. weight，value的index引用全部都-1,因为python的list的index从0开始。。。。
# 2. matrix include line 0 ( a line filled with 0), but the matrix
#    in manual don't have line 0 but begin with line 1
def knapsack_dynamic(weights, values, W_max, waitTime):
    num_objects = len(weights)
    V = createMatrix(len(weights)+1,W_max+1) 
    for j in range(1,W_max+1): V[0][j] = 0
    for i in range(1,num_objects+1):
        for j in range(0, W_max+1):
            if (j-weights[i-1] < 0): 
                V[i][j] = V[i-1][j]
            else: 
                V[i][j] = max(V[i-1][j],
                              V[i-1][j-weights[i-1]]+values[i-1])
            
            print(V[i][j], "\t", end = "")
            sys.stdout.flush()
            time.sleep(waitTime)
        print("\n")

            
    print(V)

# optimize space complexity: use only one array
def knapsack_dynamic_SpaceN(weights, values, W_max):
    num_objects = len(weights)
    V = [0]*(W_max+1) 

    for i in range(1,num_objects+1):
        for j in range(0,W_max+1):
            j = W_max - j 
            if (j-weights[i-1] < 0): 
                V[j] = V[j]
            else: 
                V[j] = max(V[j],
                           V[j-weights[i-1]]+values[i-1])
        print(V)    

            
#If we have infinite number of objects,
def knapsack_dynamic_infinity(weights, values, W_max, waitTime):
    num_objects = len(weights)
    V = createMatrix(len(weights)+1,W_max+1) 
    for j in range(1,W_max+1): V[0][j] = 0
    for i in range(1,num_objects+1):
        for j in range(0, W_max+1):
            if (j-weights[i-1] < 0): 
                V[i][j] = V[i-1][j]
            else: 
                V[i][j] = max(V[i-1][j],
                              V[i-1][j-weights[i-1]]+values[i-1],
                              V[i][j-weights[i-1]]+values[i-1])
            
            print(V[i][j], "\t", end = "")
            sys.stdout.flush()
            time.sleep(waitTime)
        print("\n")

            
    print(V)
#knapsack_dynamic([1,2,5,6,7],[1,6,18,22,28],11,0)
#knapsack_dynamic_infinity([1,2,5,6,7],[1,6,18,22,28],11,0)
knapsack_dynamic_SpaceN([1,2,5,6,7],[1,6,18,22,28],11)




