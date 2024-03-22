a,b=0,1
n=int(input("Enter a number :"))
for i in range(n):
    c=a+b
    a=b
    b=c
    print(c,end=' ')
