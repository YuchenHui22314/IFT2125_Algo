
# function from Marc feely


def createVector(numRow):
    result = [None] * numRow
    for i in range(numRow):
        result[i] = [] 
    return result


# function from Marc feely (adapted)
def createMatrix(numRow, numCol):
    result = [None] * numRow
    for i in range(numRow):
        result[i] = [0]*numCol 
    return result

def commonsubsequence_S(S, T):
    # prend premier caractere de S:
    # et prendre une partie de T:
    commence = S[0]
    index = T.find(commence)
    T_tail = T[index:] 
    # subsequence tableau
    # subseqs_S stocke les subsequence de longeur i+1
    subseqs_S = createVector(len(T_tail))
    subseqs_S[0].append([commence,[0,0],"",True]) 
    for i in range(len(S)):
        for j in range(1,len(T_tail)):
            if S[i] == T_tail[j]:
                for k in range(len(subseqs_S)):
                    for tuple in subseqs_S[k]: 
                        string = tuple[0]
                        position = tuple[1]
                        complement = tuple[2] 
                        if (i > position[0]) and (j > position[1]):
                            subseqs_S[k+1].append([string+S[i], [i,j],complement,True])
        for liste in subseqs_S:
            for tuple in liste:
                if tuple[3] == False:
                    tuple[2] += S[i]
                tuple[3] = False
                            

    result = [None]*len(T_tail)     
    for k in range(len(subseqs_S)):
        text = "subsequence de longeur " + str(k+1) + " sont" 
        ensemble = set();
        for pair in subseqs_S[k]: 
            string = pair[0]
            ensemble.add(string)
        result[k] = ensemble
        for string in ensemble:
            text += " " + string + " "

        print(text)
        
    print(subseqs_S)
    return (result,subseqs_S)


# commonsubsequence_S("AGCAT", "ACAGT")
# commonsubsequence_S("GTACA", "AGCAT",)
# commonsubsequence_S("AGCAT","GTACA")
# commonsubsequence_S("ABBC", "ABCB",)

#On assume que len(Z) = len(X) + len(Y)
#retournera si Z est dans le shuffle de X et Y (oui -> Ture, non -> False)
def Z_inShuffle_XY(X,Y,Z):
    
    lenX = len(X)
    lenY = len(Y)
    
    #base case:
    if (lenX == 0):
        return Y == Z
    if (lenY == 0):
        return X == Z

    #initialisation:
    T = createMatrix(lenX + 1, lenY + 1)
    # Z[0:0] \in shuffle of X[0:0] et Y[0:0]  
    T[0][0] = True   
    for i in range(1,lenX+1):
        # Z[0:i] \in shuffle of X[0:i] et Y[0:0] ????
        T[i][0] = (X[i-1] == Z[i-1]) and (T[i-1][0] == True) 
    for j in range(1,lenY+1):
        # Z[0:i] \in shuffle of Y[0:i] et X[0:0] ????
        T[0][j] = (Y[j-1] == Z[j-1]) and (T[0][j-1] == True) 
    

    #Remplissage du tableau
    #recurrence : 
    #   1) Z[0:i+j-2] est dans le shuffle de X[0:i-1] et Y[0:j-2] et 
    #  et Z[0:i+j-1] == X[i-1]
    #       Ou bien ------------------
    #   1) Z[0:i+j-2] est dans le shuffle de X[0:i-2] et Y[0:j-1]
    #  et Z[0:i+j-1] == Y[i-1]
    #  ===================> \implique 
    # Z[0:i+j-1] est dans le shuffle de X[0:i-1] et Y[0:j-1]   

    for i in range(1, lenX + 1):
        for j in range(1, lenY + 1):
            T[i][j] = (((T[i-1][j] == True) and (X[i-1] == Z[i+j-1])) 
            or ((T[i][j-1] == True) and (Y[j-1] == Z[i+j-1])))
        if (X == "ADEF") and (Y == "BCG"):
            print (T[i])


    return (T[lenX][lenY] == True)


# len(s) == len(T), sinon rien n'est assure
def Question2(S, T):
    if S[0] == T[0]:
        candidates = commonsubsequence_S(S,T)[1]
        for liste in candidates:
            for tuple in liste:
                if (Z_inShuffle_XY(tuple[0],tuple[2],T) == True):
                    print("X", tuple[0], "Y",tuple[2]);
                    return True

        
    Xcandidates = commonsubsequence_S(S,T)[0]
    Ycandidates = commonsubsequence_S(T,S)[0]
    n = len(S)
    for i in range(len(Xcandidates)):
        for X in Xcandidates[i]:
            lenX = i+1
            lenY = n-lenX
            if (lenY == 0):
                return ((Z_inShuffle_XY(X,"",S)) and (Z_inShuffle_XY(X,"",T))) 
            j = lenY-1
            if len(Ycandidates)-1 >= j: 
                for Y in Ycandidates[j]:
                    result = ((Z_inShuffle_XY(X,Y,S)) and (Z_inShuffle_XY(X,Y,T))) 
                    if result == True:
                        print("X", X, "Y",Y);
                        return result

 
print(Question2("ABCDEFG", "BCGADEF"))
