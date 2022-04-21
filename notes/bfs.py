graph = {}
graph[1] = [2,3,4]
graph[2] = [3,5,6]
graph[3] = [1,2,6]
graph[4] = [1,7,8]
graph[5] = [2,6]
graph[6] = [2,3,5]
graph[7] = [4,8]
graph[8] = [4,7]

visited = {i:False for i in range(1,9)} 
print(visited)

def bfs(v):
    queue = []
    queue.insert(0,v)   # enqueue
    visited[v] = True
    while queue:    #queue is true when it is not empty.
        node = queue.pop()
        # setting false can not be put here !!!!!!!!!!
        #-------------- or other visit operation -----
        print(node)                               #---
        #-------------- or other visit operation -----
        for neighbor in graph[node]:
            if visited[neighbor] == False:
                queue.insert(0,neighbor)
                # it is important to set visited false here.
                # other than at !!!!!!!!! 
                visited[neighbor] = True
        #print(queue)

def dfs_stack(v):
    stack = []
    stack.append(v)
    visited[v] = True
    while stack:
        while True:
            node_under_consideration = -1
            top = stack[-1]    # peek
            #-------------- or other visit operation -----
            print(top)                          #---
            #-------------- or other visit operation -----
            for neighbor in graph[top]:
                if visited[neighbor] == False:
                    node_under_consideration = neighbor
                    break
            if node_under_consideration == -1:
                break
            stack.append(node_under_consideration)
            visited[node_under_consideration] = True
        stack.pop()
        


def search(graph):
    for node in graph.keys():
        if visited[node] == False:
            dfs_stack(node)

search(graph)
