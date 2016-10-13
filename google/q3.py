import math
import sys

def answer(total_lambs):
    # your code here
    
    na=math.floor(math.log(total_lambs+1,2))
    na=int(na)
    nb=0
    if total_lambs<=2:
    	nb=total_lambs
    else:
    	nb=2
    	total_lambs-=nb
    	prev=[1,1]
    	while(total_lambs>=prev[0]+prev[1]):
    		total_lambs-=prev[0]+prev[1]
    		temp=prev[0]
    		prev[0]=prev[1]
    		prev[1]=prev[1]+temp
    		nb+=1

    # print na,nb
    return nb-na

print answer(sys.maxint)
