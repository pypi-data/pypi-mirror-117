def triangular(n):
    for x in range(1, n+1):
        num=(x*(x+1))//2
        print(" "+str(num),end="")

num=0


def Prime(n):
    num=1
    count = 0
    while(num<=n):
        for x in range(1, num + 1):
            if(num % x)==0:
                count +=1
        if count ==2:
            print("\n " +str(num), end="")
        count=0
        num+=1

