#DFS (go deep / down before you go wide)
# use when:
#   You need to explore every connection
#   You care about paths 
#   You want to detect cycles
#   Flood Filling
#   Backtracking problems
# --> TREE RECURSION!!

def dfs(node, graph, visited): #define dfs node, graph, and visisted 
    visited.add(node) #at the visted point of the tree , add node 
    for neighbor in graph[node]: #for every neighbor in the graph at current node
        if neighbor not in visited: #if the neighbor is not in visited 
            dfs(node, graph, visited) #recursuvely add and parse 

#BFS (visit nodes layer by layer)
# Use when you need to:
#   Shortest path in an unweighted graph
#   Level-order Traversal
#   Finding connected components quickly
# --> SHORTEST PATH, MINIMUM MOVES 

from collections import deque
def bfs(start, graph):
    q = deque([start]) #this starts the deque
    visited = {start} #visted in the dict that was started 
    while q: #while at q
        node = q.popleft() #pop left node from the node, so whatever neighbor is here 
        for neighbor in graph[node]:
            if neighbor not in visited: #if the neighbor hasn't visited,
                visited.add(neighbor) #add that neighbor
                q.append(neighbor) #append it to my deque list here. 

# Trees
# -> Each node has one parent 
# -> no cycles
# -> DFS is usually easiest

# Graphs 
# -> Edges can go in any direction
# -> Cycles are possible
# -> MUST use visited to avoid infinite loops (AE: OOOH)
# ---> This distinction matters in interviews because if you forget visited, your solution crashes.

#Island Numbers  (DFS)
def numIslands(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    def dfs(r, c):
        if (
            r < 0 or c < 0 or
            r >= rows or c >= cols or
            grid[r][c] == "0" or 
            (r, c) in visited
        ):
            return
        visited.add((r, c))

        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    count = 0 
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                dfs(r, c)
                count += 1
    return count

#Shortest Path in a Grid (BFS)
from collections import deque

def shortestPath(grid):
    rows, cols = len(grid), len(grid[0])
    q = deque([0, 0, 0])
    visited = {(0, 0)}

    while q:
        r, c, dist = q.popleft()

        if (r, c) == (rows - 1, cols - 1):
            return dist
        for dr, dc in [(1,0), (-1,0),(0,1),(0,-1)]:
            nr, nc = r + dr, c + dc

            if (
                0 <= nr < rows and
                0 <= nc < cols and 
                grid[nr][nc] == 0 and 
                (nr, nc) not in visited
            ):
                visited.add((nr, nc))
                q.append((nr, nc, dist+1))
    return -1

#Count comps (dfs)
def countComponents(graph):
    if not graph:
        return 0
    #then i need to go through and make sure to check, making sure to put down visit with the node so that it will be valid 

#valid path (bfs)
def validPath(graph, start, end):
    rows, cols = len(graph), len(graph[0])
    q = deque([start])
    visited = {start}
    while q:
        return