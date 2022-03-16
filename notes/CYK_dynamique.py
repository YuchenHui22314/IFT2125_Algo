# function from Marc feely
'''this is a function a !'''
def create_Set_Matrix(numRow,numColumn):
    result = [None] * numRow
    for i in range(numRow):
        result[i] = [set()]*numColumn
    return result


'''test pour voir si ca fonctionne...'''
# a = create_Set_Matrix(4,5)
# for i in range(0,4):
#     for j in range(0,5):
#         a[i][j] = i*j
# print(a)
        
# xiang dao CXK le ma?
# examples of G: 
# 
# {"S":["CD","DB","B"],
#  "C":["AB","AE"], 
#  "D":["DB","b"], 
#  "E":["CB"],
#  "A":["a"],
#  "B":["b"]}

# example of w "aabbb"
def CYK_dynamique(G,w):
    word_len = len(w)
    table = create_Set_Matrix(word_len+1,word_len+1)
    for i in range(1,word_len+1):
        table[i][0] = w[i-1]
        # 0 kong
        # 1 a
        # 2 a
        # 3 b
        # 4 b
        # 5 b
    for j in range(1,word_len+1): #col
        for i in range(1,word_len+1):  #rangee
            for k in range(1,word_len-(j-1)+1):
                

   