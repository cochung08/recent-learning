
class Node(object):
    def __init__(self, n):
        self.val = n
        self.distance = sys.maxint
        self.parent = None

class Solution(object):
    
        """
        :type n: int
        :rtype: int
        """
    def init(nodeArray,n):
        # nodeArray[1]=Node(1)
        nodeArray[n]=Node(n)
        if n==1:
            return 
            # input('Press <ENTER> to continue')
        if n%2==1:
            init(nodeArray,n+1)
            init(nodeArray,n-1)
            # print n
        else:
            init(nodeArray,n/2)

# nodeArray={}
# init(nodeArray,3)
# print nodeArray

    def integerReplacement(self, n):
        # your code here
        # n=int(n)
        # nodeArray=[Node(0)]
        # for num in range(1,n+2):
        #   nodeArray.append(Node(num))
    
        nodeArray={}
        init(nodeArray,n)
        Q=[]
        root=nodeArray[n]
        root.distance=0
        Q.append(root)
        result=sys.maxint
        while Q:
            current=Q.pop(0)
    
            if current.val==1:
                result=min(sys.maxint,current.distance)
                continue
    
            if current.val %2==1:
                n=nodeArray[current.val+1]
                # n=Node(current.val+1)
                if n.distance==sys.maxint:
                    n.distance=current.distance+1
                    n.parent=current
    
                    Q.append(n)
                n=nodeArray[current.val-1]
                # n=Node(current.val-1)
                if n.distance==sys.maxint:
                    n.distance=current.distance+1
                    n.parent=current
                    Q.append(n)
            else:
                # print current.val/2
    
                n=nodeArray[current.val/2]
                # n=Node(current.val/2)
    
                if n.distance==sys.maxint:
                    n.distance=current.distance+1
                    n.parent=current
                    Q.append(n)
        return result