import time
import math
def prime(n):
    d=int(math.sqrt(n))
    if(d<=100):
        for i in range(4,d):
            k=0
            for j in range(2,i):
                if(i%j==0):
                    k=k+1
            if(k==0):
                a.append(i)
        for x in range(d,n):
            z=0
            for y in range(0,len(a)):
                if(x%a[y]==0):
                    z=z+1
            if(z==0):
                a.append(x)
    else:
        prime(d)
        for x in range(d,n):
            z=0
            for y in range(0,len(a)):
                if(x%a[y]==0):
                    z=z+1
            if(z==0):
                a.append(x)
n=int(input("Enter the number:"))
a=[2,3]
prime(n)
print(a)
print(" ")
print("count",len(a))
