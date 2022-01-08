import random as rad
def pearsonR(n):
    alph=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    xs,ys,xxs,yys,xy=0,0,0,0,0
    for i in range(n):
        x=rad.randint(21,60)
        y=rad.randint(75,100)
        xs+=x
        ys+=y
        xxs+=x**2
        yys+=y**2
        xy+=x*y
        print(alph[i],"&",x,"&",y,"&",x**2,"&",y**2,"&",x*y,"\\\\")
    print(xs,ys,xxs,yys,xy)

def Ttest(n):
    xs,ys,xss,yss=0,0,0,0
    for i in range(n):
        x=rad.randint(75,100)
        y=rad.randint(75,100)
        xs+=x
        ys+=y
        xss+=x**2
        yss+=y**2
        print(x,"&",y,"&",x**2,"&",y**2,"\\\\")
    print(xs,ys,xss,yss)

def Ztest(n):
    xs,ys,xss,yss=0,0,0,0
    for i in range(n):
        x=rad.randint(75,100)
        y=rad.randint(75,100)
        xs+=x
        ys+=y
        xss+=x**2
        yss+=y**2
        print(x,"&",y,"\\\\")
    print(xs,ys)
# Ztest(30)
import math
a=[90,82,87,81,95,88,83,91,79,85,87,86]
c=[87,85,92,83,86,95,98,82,88,85,80,84]
b,d=0,0
for i in range(12):
    # b+=a[i]**2
    d+=(a[i]-86.167)**2
    # print(i,i**2)
print(math.sqrt(d/11),b)