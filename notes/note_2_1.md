```
Algo Vorace (E de candidats C)  -----> sortie : solution(S)
    S <- {}
    while C != {} et non-sol(S) do   // multi-ensemble => C 
        x <- selection(C)               // select mellieur candidat selon
        c <- C\{x}
        si completable(S U {x}) alors //feasible
            S <-  S U {x}
        fin si
    fin while
    si solution(S) alors
        return S
    else return "pas de sl"
```

Algo monnaie(C,n)
    s = 0
    S = {}
    while s != n{
        x = plus grande piece such that s+x <= n
        if no piece{
            return fail
        }
        S = S U {x}
        s = s + x
    }
    return s