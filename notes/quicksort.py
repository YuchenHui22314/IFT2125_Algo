#swap
def swap(a,b):return b,a


# will return the position of pivot after the
# side taking comportment
def pivot(liste,i,j):
    # choose casually first element of the sublist as pivot
    pivot = liste[i]

    # initialisation of left and right pointer
    l = i
    r = j

    # find the first points of swap
    # if all elements have already taken the right side, 
    # we will simply do nothing.
    # purpose is to swap T[l] et T[r] immidiately 
    # after we check l < r in each iteration, by doing
    # this we can make sure that l and r will not 
    # interlape
    
    #find first swap point for left pointer
    while True:
        if (liste[l] > pivot) or (l >= j):
            # l >= j : to avoid liste index out of range
            # and, if l = j implies well done.
            break
        l = l + 1
    #find first swap point for right pointer
    while True:
        if (liste[r] <= pivot) : 
            break
            # no and (r >= ...) because T[r] will
            # become pivot in the worst case.
        r = r - 1

    # note : we do either T[r] <= pivot or T[l] >= pivot
    # that is to say we must make sure there exists a '='
    # in either side..... reason: last step of the procedure.

    # main body
    while ( l < r ):
        # swap
        liste[r],liste[l] = swap(liste[r], liste[l])
        # move the two pointer toward center
        while True:
            if (liste[l] > pivot):
                break
            l = l + 1
        while True:
            if (liste[r] <= pivot):
                break
            r = r - 1

    # last step! swap
    liste[i],liste[r] = swap(liste[i], liste[r])
    
    # pivot position
    return r


def pivotbis(liste,i,j):
    pivot = liste[i]
    position_of_first_pivot = -1 #(not founded yet)
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
        
        #right part (more simple...)
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
            if  position_of_first_pivot == 0:
                liste[i],liste[right] = swap(liste[i],liste[right]) 
                return right, right + 1
            else:
                liste[i],liste[position_of_first_pivot-1] = swap(liste[i],liste[position_of_first_pivot-1])
                position_of_first_pivot -= 1
                return  position_of_first_pivot - 1, left
                
                
            

        


def quicksort(liste,i,j): 
    length = j - i + 1 
    if length == 0 or length == 1:
        return 
    if length == 2:
        if liste[i] < liste[j]:
            return 
        liste[i],liste[j] = swap(liste[i], liste[j])
        return
    pivotIndex = pivot(liste,i,j)
    quicksort(liste,i,pivotIndex-1) 
    quicksort(liste,pivotIndex+1,j) 

a = [2, 5, 3, 7, 2, 4, 9, 10, 20394, 333,-1]
b = [3,2,3,4,5,6,3,1,3,8,3,9]
print(a)
lenth = len(a)
quicksort(a,0,lenth-1)
print(a)
print(b)
ll,rr = pivotbis(b,0,len(b)-1)
print(b)
print(ll,rr)

