import sys
class Node(object):
    def __init__(self, n):
        self.val = [n/8,n%8]
        self.distance = sys.maxint
        self.parent = None

def answer(src,dst):
    if src==dst:
        return 0
    maze=[]
    for i in range(0,64):
        maze.append(Node(i))
        # print maze[-1].val
    Q=[]
    maze[src].distance=0
    Q.append(maze[src])

    while Q:
        current=Q.pop(0)
        # print current.val
        # moves=[-8*2-1,-8*2+1,+8*2-1,+8*2+1,-2-8*1,-2+8*1,+2-8*1,+2+8*1]
        moves=[[-2,-1],[-2,1],[2,-1],[2,1],[-1,-2],[1,-2],[-1,2],[1,2]]
        for m in moves:
            # adjacent to current and within bound
            x=current.val[0]+m[0]
            y=current.val[1]+m[1]
            if x>=0 and x<=7 and y>=0 and y<=7:
                adj=x*8+y
                # print adj,x,y
                if maze[adj].distance==sys.maxint:
                    maze[adj].distance=current.distance+1

                    if adj==dst:
                        return maze[adj].distance
                    maze[adj].parent=current.val

                    Q.append(maze[adj])


print answer(0,1)
print answer(19,36)
print answer(0,0)
print answer(20,36)
print answer(23,39)
print answer(15,16)








        

    