#
# x = list(range(n));
n = 1
def sacadosVor(W,w,v):
    x = list(range(n)) 
    C = 0;
    while C < W:
        i = selectionLocal(w,v);
        if C + w[i] <= W:
            x[i] = 1                      #choisie
            C = C + w[i]
        else:
            x[i] = (W - C)/w[i]      #une partie
            C = W
    return x

#objet de + grande valeur, 
#but:sugmenter la valeur dans le sac le 
#plus vite que possible
# def selectionLocal_1(w,v):
    
#objet le + leger
#but: plus d'objets possible et donc d'avoir plus la valeur
# def selectionLocal_2(w,v):

#objet avec unite de poid max
#melange des deux derniers
# def selectionLocal_3(w,v):

w = [10,20,30,40,50]
v = [20,30,60,40,60]
print(zip(w,v))
rou = list(map(lambda x : float(x[0]/x[1]), zip(w,v)))
print(rou)

a=(10,20)
b = a[0]/a[1];
print(b)
