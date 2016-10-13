import math

# def ps(n):
# 	root_of_n = math.sqrt(n)
# 	decimal_of_root = root_of_n - int(root_of_n)
# 	if decimal_of_root < 0.5:
#   		return int(root_of_n)**2
# 	else:
#   		return (int(root_of_n)+1)**2


def answer(n):
    # your code here

    n=int(n)
    if n<1:
    	return 0
    # perfectSq=ps(n)
    # print n
    a=abs(2**math.ceil(math.log(n,2)) -n)+math.ceil(math.log(n,2))
    b=abs(2**math.floor(math.log(n,2)) -n)+math.floor(math.log(n,2))
    return int(min(a,b))
    # return int(math.log(perfectSq,2))+abs(perfectSq-n)

    # if n<=1:
    # 	return n
    # if n%2==0:
    #     return int(math.log(n,2))
    # else:
    #     return int(math.log(n+1,2)+1)

print answer(0)

print answer(1)
print answer(3)
print answer(4)
print answer(5)
print answer(15)
print answer(27)

