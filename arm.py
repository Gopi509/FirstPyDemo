n=int(input("Enter a number :"))
s=0
t=n
while(n>0):
    digits=t%10
    s=s+digits**3
    t=t//10
if(n==s):
    print(n,"is an Armstrong number")
else:
    print(n,"is Not an Armstrong number")
