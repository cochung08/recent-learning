import math
import sys
import os
class Node(object):
    def __init__(self, n):
        self.val = n
        self.distance = sys.maxint
        self.parent = None


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

def answer(n):
    # your code here
    n=int(n)
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
def integerReplacement(n):
    if n == 1: return 0
    if n & 1 == 0: return integerReplacement(n / 2) + 1
    return min(integerReplacement(n + 1), integerReplacement(n - 1)) + 1

# print answer(444444444444444444444444444444444444444444444444444444444444)

# print answer(1)
# print answer(3)
# print answer(4)
# print answer(5)
print answer(7)
print integerReplacement(7)

print answer(15)
print integerReplacement(15)
print answer(27)
print integerReplacement(27)

# print answer(1000000)
# print integerReplacement(1000000)
