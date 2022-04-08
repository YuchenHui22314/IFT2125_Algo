from sys import argv
def n_queens(n):
    solution_vector = [0]*n
    
    def queens (k, already_chosen_list, diag45, diag135):
        if k == n:
            print(solution_vector)
        else:
            for j in range(1, n+1):
                if (j not in already_chosen_list) and (j-k not in diag45) and (j+k not in diag135):
                    solution_vector[k] = j
                    new45 = diag45.copy()
                    new45.add(j-k)
                    new135 = diag135.copy()
                    new135.add(j+k)
                    queens(k+1, solution_vector[0:k+1], new45, new135)
        
    queens(0, [], set(), set())

n_queens(int(argv[1]))
