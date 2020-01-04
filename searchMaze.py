# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

grid2 = [[0,0,0],
         [0,1,1],
         [0,0,0]]

goal2 = [len(grid2)-1, len(grid2[0])-1]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']



def search(grid,init,goal,cost):
    '''
    Try iteratively to move to next level, mark visited2, add to list of next level starting points if 
    it's a new node
    '''
    # make visited array initialized to 0, mark 1 when visited
    visited = grid[:]
    visited[:] = [[0] * len(visited[0]) for _ in range(len(visited))]
    #mark init as visited
    visited[0][0] = 1
    print(visited)
    print("grid: {}\n".format(grid))
    #list of lists of levels
    path = [[init]]
    curr_cell = init
    #try each of curr_level to find possible moves
    curr_level =[]
    #append possible move-to cells to next_level
    next_level = []
    # how many moves to get to goal
    num_moves = 0
    # counters
    i,j,k,l = 0,0,0,0
    #flag to break outer while loop
    get_out = False
    while(get_out==False):
        # set curr_level
        curr_level = [x[:] for x in path[i]]
        print("i: {} curr_level: {}\n".format(i, curr_level))
        #iterate curr_level to find moves for each cell in curr_level
        #append to next_level
        for j in range(len(curr_level)):
            #iterate level and set each cell to curr_cell
            curr_cell = curr_level[j]
            print("j: {} curr_cell: {}".format(j, curr_cell))
            #check if curr_cell is goal then break inner loop
            if curr_cell == goal:
                get_out = True
                break
            row = curr_cell[0]
            col = curr_cell[1]
            #try up
            if row-1 >=0:
                if grid[row-1][col]!=1 and visited[row-1][col]!=1:
                    #append to next level
                    next_level.append([row-1, col])
                    #mark as visited
                    visited[row-1][col]=1
            # try left
            if col-1 >=0:
                if grid[row][col-1]!=1 and visited[row][col-1]!=1:
                    #append to next level
                    next_level.append([row, col-1])
                    #mark as visited
                    visited[row][col-1]=1
            # try down
            if row +1 < len(grid):
                if grid[row+1][col]!=1 and visited[row+1][col]!=1:
                    #append to next level
                    next_level.append([row+1, col])
                    #mark as visited
                    visited[row+1][col]=1
            # try up
            if col+1 < len(grid[0]):
                if grid[row][col+1]!=1 and visited[row][col+1]!=1:
                    #append to next level
                    next_level.append([row, col+1])
                    #mark as visited
                    visited[row][col+1]=1
        # done iterating, append next level to path
        temp = next_level[:]
        path.append(temp)
        print("path w/next_level: {}\n".format(path))
        # reset next_level
        next_level[:]=[]
        #increment counter
        i +=1
    
    #found curr_cell== goal in curr_level without appending next_level
    #i-1 for num moves since i starts at 0 for init and increments for each level and we found curr_cell==goal
    # in the i'th level
    num_moves = i-1
    # set path to format [optimal path length, row, col]
    path = [num_moves, curr_cell[0], curr_cell[1]]
            
    return path

if __name__ == "__main__":
    # test on small 3*3 grid
    #path2 = search(grid2, init, goal2, cost)
    #print("found path: ", path2)

    # test on main grid
    path = search(grid, init, goal, cost)
    print("found path: ", path)
