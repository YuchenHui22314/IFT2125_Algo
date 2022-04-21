import math
#global variable:
w = [2,3,4,5]
v = [3,5,6,10]
n = 4
total_weight = 8
# en fait, the way this algo traverses all possibilities
# is a general template for all the situation
# where we are to choose from n types of items
# and we can choose each type of items infinit times

# this procedure just return one possible solution (value + composite)

def backtracking_snapsack(i,reste_weight):
    #--
    total_value = 0
    total_item_liste = [[i] for i in range(n)]
    #--
    choix = n + 65536   # \inf
    for j in range(i,n):
        if w[j] <= reste_weight:

            value_added,items_chosen = \
            backtracking_snapsack(j,reste_weight - w[j])

            value_total = value_added + v[j]
            total_item_liste[j].extend(items_chosen)

            if value_total >= total_value:
                choix = j
                total_value = value_total

    if choix <= n-1 :  # at least a item is chosen
        return total_value,total_item_liste[choix]
    else:
        return total_value,[]

print(backtracking_snapsack(0,total_weight))

