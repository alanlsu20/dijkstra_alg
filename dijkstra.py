from math import inf

#Needs:
#grid.nodes as list containing all nodes
#grid.size as number of nodes. or just len(grid.nodes)
#node.adj as list of what is adjacent to 
#node.dist as list of distances correlating to adjacency list

def dijkstra_alg(current, visited, pathlist, distlist, "some implementation of grid"):
    """Using recursive scheme. Generates list of shortest path to every
        node from start point."""
    if all(visited)==True:
        return 
    for i in range(len(current.adj)):#needs to be integrated with class
        c=current.adj[i]
        if c in pathlist[current]:#prevents reanalyzing previous node
            continue
        totaldist=c.dist[i]+distlist[current]
        if totaldist<distlist[c]:
            distlist[c]=totaldist
            pathlist[c]=current
        elif totaldist==distlist[c]:
            pathlist[c].append(current)
    visited[current]=True
    for i in range(len(current.adj)):
        c=current.adj[i]
        if visited[c]==False:
            dijkstra_alg(c,visited,pathlist,distlist, grid) #recursively runs dijkstra_alg until all nodes visited

def path_printer(start,end,pathlist,distlist):
    print("Shortest path from {} to {}:" .format(start,end))
    current=end
    while current!=start:
        if current==end:
            travelpath=str(current)
        else:
            travelpath=str(current)+" -> "+travelpath
        current=pathlist[current]
    travelpath=str(start)+" -> "+travelpath
    print(travelpath)
    print("Length is: {}" .format(pathlist[end]))
    
def dijkstra(grid,start,end):
    if start not in grid.nodes:#needs to be integrated
        return "Not acceptable input, try again."
    #initializing pathlist and distlist and visited
    visited={}
    for i in range(grid.size):
        visited{str(grid.nodes[i])}=False
    pathlist={}
    for i in range(grid.size):
        path{str(grid.nodes[i])}=None
    distlist={}
    for i in range(grid.size):
        if grid.nodes[i]=start:
            distlist{str(start)}=0
            pass
        else:
            dist{str(grid.nodes[i])}=inf
    dijkstra_alg(start,visited,pathlist,distlist)
    print("Shortest path to all points in grid calculated using Dijkstra's Algorithm.")
    flag=True
    while flag=True
        end=input("Where do you want to go from {}?:" .format(start))
        if end in grid.nodes:
            path_printer(start,end,pathlist,distlist)
            print("")
            marker=input("Try another point? (y/n):")
            if marker="n":
                flag=False
        else:
            print("Input not understood. Try entering the name of a node or 'all' to print all shortest paths.)
            print("Acceptable inputs are:")
            for i in range(grid.size):
                if grid.nodes[i]!=start:
                    print(grid.nodes[i])
                    
            
                    
    
    
        