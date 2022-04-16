#author: Yuchen Hui
#date : 22-03-17
import sys

# function from Marc feely
'''this is a function a !'''
def create_Set_Matrix(numRow,numColumn):
    result = [None] * numRow
    for i in range(numRow):
        result[i] = [] 
        for j in range(numColumn):
            result[i].append([])

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
def CYK_dynamique(Grammar,word):
    word_len = len(word)
    table = create_Set_Matrix(word_len+1,word_len+1)
    for i in range(1,word_len+1):
        table[i][0] = word[i-1]
        #   0    1      2     3   
        # 0 kong kong   kong
        # 1 a    A
        # 2 a    A
        # 3 b    B,D
        # 4 b    B,D
        # 5 b    B,D
    for c in range(1,word_len+1): #col
        for i in range(1,word_len-(c-1)+1):  
            #number of row worth consideration
            #decreases when col augment, 
            #as demonstrated in the comment above...
            
            if c == 1 :
                for left,rights in Grammar.items():
                    terminal = table[i][0] 
                    if terminal in rights:
                        table[i][c].append(left)  
                continue
            # c != 1:
            for c1 in range(1,c):   
                 # values in colomn c depends on values
                 # in colomns 1~c-1.
                 for prefix in table[i][c1]:
                     for postfix in table[i+c1][c-c1]:
                         combination = prefix + postfix
                         for left,rights in Grammar.items():
                             if combination in rights:
                                 table[i][c].append(left)
    for yuyanggege in range(word_len+1):
        for yuyangxiong in range(word_len+1):
            print(table[yuyanggege][yuyangxiong]," ",end = "")
        print("\n",end="")
    return ("S" in table[1][word_len])
                
grammar1 = {"S":["CD","DB","B"],
 "C":["AB","AE"], 
 "D":["DB","b"], 
 "E":["CB"],
 "A":["a"],
 "B":["b"]}
word = "aabbb"


print(CYK_dynamique(grammar1,word))
   
