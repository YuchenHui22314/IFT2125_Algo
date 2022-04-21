import math
#swap
def swap(a,b): return b,a

#pivotbis
def pivotbis_weak(liste,i,j):
    pivot = liste[i]
    position_of_first_pivot = -1 #(not found yet)
    left = i+1
    right = j

    #main loop
    while True :
        #left part
        while True:
            if liste[left] > pivot or left >= j:
                break
            if liste[left] == pivot and position_of_first_pivot == -1:
                position_of_first_pivot = left 
            if (liste[left] < pivot) and (position_of_first_pivot > 0):
                liste[left],liste[position_of_first_pivot] = swap(liste[left],liste[position_of_first_pivot])
                position_of_first_pivot += 1
            left += 1
        
        #right part (simpler...)
        while True:
            if liste[right] <= pivot:
                break
            right -= 1

        #swap left and right
        #after swap if liste[left] < pivot
        if (left < right):
            liste[left],liste[right] = swap(liste[left],liste[right]) 
            if liste[left] < pivot:
                liste[left],liste[position_of_first_pivot] = swap(liste[left],liste[position_of_first_pivot])
                position_of_first_pivot += 1
                
        else: ## note : there is no way that left = right, why?
            #fin
            # if q = 0, it is like in pivot()
            if  position_of_first_pivot == -1:
                liste[i],liste[right] = swap(liste[i],liste[right]) 
                return right, right + 1
            else:
                liste[i],liste[position_of_first_pivot-1] = swap(liste[i],liste[position_of_first_pivot-1])
                position_of_first_pivot -= 1
                return  position_of_first_pivot - 1, left


def pivotbis(liste,pivot,i,j):
    position_of_first_pivot = -1 #(not found yet)
    left = i
    right = j

    #main loop
    while True :
        #left part
        while True:
            if liste[left] == pivot and position_of_first_pivot == -1:
                position_of_first_pivot = left 
            if (liste[left] < pivot) and (position_of_first_pivot > 0):
                liste[left],liste[position_of_first_pivot] = swap(liste[left],liste[position_of_first_pivot])
                position_of_first_pivot += 1
            if left >= j or liste[left] > pivot:
                break
            left += 1
        
        #right part (simpler...)
        while True:
            if liste[right] <= pivot:
                break
            right -= 1

        #swap left and right
        #after swap if liste[left] < pivot
        if (left < right):
            liste[left],liste[right] = swap(liste[left],liste[right]) 
            if liste[left] < pivot and position_of_first_pivot != -1:
                liste[left],liste[position_of_first_pivot] = swap(liste[left],liste[position_of_first_pivot])
                position_of_first_pivot += 1
                
        else: ## this is wrong: note : there is no way that left = right, why?
            if left == right:
                #if left == right, then list[left] == pivot 
                return position_of_first_pivot-1, left+1
                # left + 1 out of range, but it is ok.

            # if left > right, then liste[left] > pivot,
            # and liste[left] is the first such element.
            # there is no way position_of_first_piovt == -1
            return  position_of_first_pivot - 1, left



test_array = [-655536,-1,3,0,3,1,3,2,3,3,3,4,3,5,3,6,3,7,3,8,3,9,3]
print(test_array)
ll,rr = pivotbis(test_array,3,0,len(test_array)-1)
print(test_array)
print(ll,rr)
print(test_array.index(7))

## selection
def selection(liste,s):
    i = 0
    j = len(liste) - 1
    while True:
        pivot = pseudomed(liste[i:j+1])
        l,r = pivotbis(liste,pivot,i,j)
        if s <= l : j = l
        elif s >= r : i = r
        else: return pivot

## adhoc: sort and take the ceil(n/2)th element
def adhocmed(liste):
    n = len(liste)
    median_pos = int(math.ceil(n/2))-1 
    liste.sort()
    return liste[median_pos]

def pseudomed(liste):
    n = len(liste)
    if n <= 5: return adhocmed(liste)
    z = int(math.floor(n/5))
    Z = []
    for i in range(z):
        Z.append(adhocmed(liste[5*i:5*i+5]))
    return selection(Z,int(math.ceil(z/2))-1)

test_liste = [1,6,4,7,8,9,2,6,6,10,13,12,11]
print(test_liste)
print(selection(test_liste, int(math.ceil(len(test_liste)/2))-1))
print(test_liste)
