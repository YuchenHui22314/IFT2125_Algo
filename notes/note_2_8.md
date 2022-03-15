PRIM & Dijkstra

comme pour prim, on numerote les sommets de 1 a n, 1 etant la source. ON garde en memoire le poies des aretes dans une matrice L(nxn), avec L[i,j]=infini si aucune arete entre i et j.

on va maintenir une liste D de longeur n, qui contiendra a la fin de l<algo> ,les distances minimale entre la source et les sommets

on va aussi maintenir une liste P ( precedent) ou p[i] contien le sommet qui precede i sur le chemin minimal entre la source et i

Algo vorace Dijkstra(matrice L,liste P) : 
    D <- nouvelle liste avec len = n
    P <- nouvelle liste avec len = n
    C <- {2,3,,,,,n}
    for i in range(2,n+1):
        D[i] = L[i][1]
        P[i] = <- 1
    repeter n-2 fois:
        v = element i dans c avec D[i] minimale
        c = c\{i} 
        pour chaque element w de c faire
            D[w] = min{D[w],D[v]+L[v,w]} 
            if D[w]=D[v]+L[v,w] :
                P[w] = v

Proposition : Dans algorithm Dijkstra, chaque fois qu'un sommet u est selectionne D{u} est le cout d"un chemin minimal entre lea source et u et ce chemin est compose seulement de sommets et d'arets deja selectionnes.

Preuve: (Par contradiction)
v est la source
supposons le contraire: i.e. que lorsqu'on selecionne u, D[u] est > d(v,u) et que le chemin entre v et u passe par un sommet z pas encore selectionne.

juste avant de choisir le sommet u : 

v->y->z->u
d(y) = d(v,y)
d(z) <= d(y) + poids(y,z)

on a d(v,u)  =d<v,z>+d<z,u> et d<z,u> > 0