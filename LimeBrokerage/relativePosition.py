
def  optimalRelativePaths( paths):
    res=[]
    res.append(0)
    res.append(0)
    print res
    r=[]
    for it,val in enumerate(paths):
        print it
        if it%2==0:
            if it=='U':
                res[0]=int(res[0])+int(paths[it+1])
            elif it == 'D':
                res[0]=int(res[0])-int(paths[it+1])
            elif it == 'R':
                res[1]=int(res[1])+int(paths[it+1])
            elif it== 'L':
                res[1]=int(res[1])-int(paths[it+1])
                
    if res[0] >0:
        r.append('U')
    else:
        r.append('D')
    r.append(abs(res[0]))  
                
    if res[1] >0:
        r.append('R')
    else:
        r.append('L')
    r.append(abs(res[1]))
    
    return r


print optimalRelativePaths('U2R3')
