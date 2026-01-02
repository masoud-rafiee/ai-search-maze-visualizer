from pyamaze import maze, agent,COLOR, textLabel
from queue import PriorityQueue
import time

def BFS(m):
    start = (m.rows,m.cols)  #since m.rows and m.col is the # of rows and columns , it start from bottom-right cell
    tovisit=[start]          #holding the cells that need to be explored
    visited = [start]        #tracking what has been visited already
    bfsPath={}               #dictionary to keys: current cell and values: where it came from (to store the path the snake has traversed)
    nodes_expanded = 0  # Initialize counter
    while len (tovisit)>0:   #if any cells left to visit
        thisCell=tovisit.pop(0)#going to the cell that needs to be explored (next)
        nodes_expanded += 1  # Increment counter
        if thisCell == (1,1): #since our goal is at 1,1 so if we have reached there we should stop
            break
#as bfs requires, we check which neighbors are acessible
        Directions=['E', 'S', 'N', 'W']        
        for direction in Directions:        #checking each direction east,south,north and west to see if any open
            if m.maze_map[thisCell][direction]==True:
                if direction=='E':
                    childCell=(thisCell[0],thisCell[1]+1)#move east
                elif direction=='W':
                    childCell=(thisCell[0],thisCell[1]-1)#move west
                elif direction=='N':
                    childCell=(thisCell[0]-1,thisCell[1])#move north
                elif direction=='S':
                    childCell=(thisCell[0]+1,thisCell[1])#move south
                if childCell in visited: #don't add if it has already been explored 
                        continue    
                tovisit.append(childCell)     #adding valid neighbor to the queue
                visited.append(childCell)  
                bfsPath[childCell]=thisCell#tracking the path from this cell to next
#for security,making a path reconstruction (not losing where we came from)
    fwdpath ={}             #now a new dictionary for reconstrcuted path from goal to start
    cell = (1,1)            #since we start reconstructing back from the goal to start 
    while cell!=start:      #untill reaching start point
        fwdpath[bfsPath[cell]]=cell#recording path from parent of cell to cell and so on
        cell=bfsPath[cell] #moving backward from goal to start
    return fwdpath, nodes_expanded

def DFS(m):
    start = (m.rows,m.cols)  #since m.rows and m.col is the # of rows and columns , it start from bottom-right cell
    visited = [start]        #tracking what has been visited already
    tovisit=[start]          #holding the cells that need to be explored
    dfsPath={}               #dictionary to keys: current cell and values: where it came from (to store the path the snake has traversed)
    nodes_expanded = 0  # Initialize counter
    while len (tovisit)>0:   #if any cells left to visit
        thisCell=tovisit.pop()#going to the cell that needs to be explored (next)
        nodes_expanded += 1  # Increment counter
        if thisCell == (1,1): #since our goal is at 1,1 so if we have reached there we should stop
          break
#as dfs requires, we check which neighbors are acessible
        Directions=['E', 'S', 'N', 'W'][::-1]  # Reverse order        
        for direction in Directions:           #checking each direction east,south,north and west to see if any open
            if m.maze_map[thisCell][direction]==True:
                if direction=='E':
                    childCell=(thisCell[0],thisCell[1]+1)#move east
                elif direction=='W':
                    childCell=(thisCell[0],thisCell[1]-1)#move west
                elif direction=='N':
                    childCell=(thisCell[0]-1,thisCell[1])#move north
                elif direction=='S':
                    childCell=(thisCell[0]+1,thisCell[1])#move south
                if childCell in visited:      #don't add if it has already been explored 
                        continue    
                visited.append(childCell)
                tovisit.append(childCell)     #adding valid neighbor to the queue
                dfsPath[childCell]=thisCell#tracking the path from this cell to next
#for security,making a path reconstruction (not losing where we came from)
    fwdpath ={}              #now a new dictionary for reconstrcuted path from goal to start
    cell = (1, 1)            #since we start reconstructing back from the goal to start 
    while cell!=start:       #untill reaching start point
        fwdpath[dfsPath[cell]]=cell#recording path from parent of cell to cell and so on
        cell=dfsPath[cell]   #moving backward from goal to start
    return fwdpath,nodes_expanded

def h(location,goal):        #calcualting the manhatan distance
        x1,y1=location
        x2,y2=goal
        return abs(x1-x2)+abs(y1-y2)

def Astar(m):
    start=(m.rows,m.cols)
    g_of_n={cell: float ('inf') for cell in m.grid}#each cell assigned as infinite in grid (maze)
    g_of_n[start]=0
    f_of_n={cell:float ('inf') for cell in m.grid}
    f_of_n[start]=h(start,(1,1))
    open=PriorityQueue()
    open.put((h(start, (1, 1)), h(start, (1, 1)), start))
    nodes_expanded = 0
    StarPath={}

    while not open.empty():
        thisCell = open.get()[2]  # Get the cell to explore
        nodes_expanded += 1

        if thisCell==(1,1):
            break
        Directions=['E', 'S', 'N', 'W']
        for direction in Directions:        #checking each direction east,south,north and west to see if any open
            if m.maze_map[thisCell][direction]==True:
                if direction=='E':
                    childCell=(thisCell[0],thisCell[1]+1)#move east
                elif direction=='W':
                    childCell=(thisCell[0],thisCell[1]-1)#move west
                elif direction=='N':
                    childCell=(thisCell[0]-1,thisCell[1])#move north
                elif direction=='S':
                    childCell=(thisCell[0]+1,thisCell[1])

                tmp_g=g_of_n[thisCell]+1
                tmp_f=tmp_g+h(childCell,(1,1))

                if tmp_f<f_of_n[childCell]:
                    g_of_n[childCell]=tmp_g
                    f_of_n[childCell]=tmp_f
                    open.put((tmp_f,h(childCell,(1,1)),childCell))
                    StarPath[childCell]=thisCell

    # Reconstruct the path
    fwdpath = {}
    cell = (1, 1)
    while cell != start:
        fwdpath[StarPath[cell]] = cell
        cell = StarPath[cell]

    return fwdpath, nodes_expanded

if __name__=='__main__':
    m = maze(13,13) #create a 13*13 maze
    m.CreateMaze(theme=COLOR.dark,loopPercent=33)
    
    start_time_bfs= time.time() #record for bfs start
    PATH, bfs_nodes= BFS(m)
    end_time_bfs = time.time()
    time_taken_bfs=end_time_bfs-start_time_bfs
    
    start_time_dfs=time.time()
    path, dfs_nodes= DFS(m)
    end_time_dfs = time.time()
    time_taken_dfs=end_time_dfs-start_time_dfs
    
    start_time_a = time.time()
    Spath, star_nodes= Astar(m)
    end_time_a=time.time()
    time_taken_a = end_time_a-start_time_a
    

    A = agent(m,footprints=True,color=COLOR.red, shape='filled_circle')
    A2 = agent(m,footprints=True,color=COLOR.green, shape='filled_circle')
    A3 = agent(m,footprints=True,color=COLOR.blue, shape='filled_circle')

    m.tracePath({A: PATH}, delay=50)
    m.tracePath({A2:path}, delay=50)
    m.tracePath({A3: Spath}, delay=50)
    #print("Tracing path:", PATH)
    #Display Nodes Expanded
    l = textLabel(m, 'RED: Length of shortest path BFS: ', len(PATH) + 1)
    l2 = textLabel(m, 'GREEN: Length of shortest path DFS: ', len(path) + 1)
    l6 = textLabel(m, 'BLUE: Length of shortest path A*: ', len(Spath) + 1)
    l3 = textLabel(m, 'Nodes Expanded BFS: ', bfs_nodes)
    l4 = textLabel(m, 'Nodes Expanded DFS: ', dfs_nodes)
    l5 = textLabel(m, 'Nodes Expanded A*: ', star_nodes)
    print("Nodes Expanded BFS:", bfs_nodes)
    print('Length of shortest path BFS: ', len(PATH) + 1)
    print(f"BFS took {time_taken_bfs:.6f} seconds")
    print("Nodes Expanded DFS:", dfs_nodes)
    print('Length of shortest path DFS: ', len(path) + 1)
    print(f"DFS took {time_taken_dfs:.6f} seconds")
    print("Nodes Expanded A*:", star_nodes)
    print('Length of shortest path A*: ', len(Spath) + 1)
    print(f"A* took {time_taken_a:.6f} seconds")
    
    

    m.run()

