n=int(input("Enter the number :"))
s=0
temp=n
while(temp>0):
    digits=temp%10
    s=s+digits**3
    temp=temp//10
if(n==s):
    print("Amstrong Number ")
else:
    print("Not a Armstrong Number")
    
    
