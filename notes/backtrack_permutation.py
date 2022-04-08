def permutation(n):
    T = list(range(1,n+1))
    TT = list(range(1,n+1))

    def perm(i):
        if i == n:
            print(T)
        else:
            for j in range (i,n+1):
                #exchange T[i] et T[j]
                temp = T[i-1]
                T[i-1] = T[j-1]
                T[j-1] = temp
                #recursive call
                perm(i+1)
                #recursive call
                #exchange T[i] et T[j]
                temp = T[i-1]
                T[i-1] = T[j-1]
                T[j-1] = temp

    def perm_another_version(i):
        if i == n:
            print(TT)
        else:
            for j in range(1, n+1):
                if j not in TT[0 : i]:
                    TT[i] = j
                    perm_another_version(i+1)

    perm_another_version(0)
    #perm(1)

permutation(4)
