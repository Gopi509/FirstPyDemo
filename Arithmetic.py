a=int(input("Enter the first number :"))
b=int(input("Enter the second number  :"))
operations=('+','-','*','%','/')
print("Select the operation which you need to perform :",operations)
choice=input("enter symbol :")
if(choice=='+'):
    print("Sum of the two numbers is",a+b);
if(choice=='-'):
    print("Minus of the two numbers is",a-b);
if(choice=='%'):
    print("Modulo of the two numbers is",a%b);
if(choice=='*'):
    print(" Multiplication of  the two numbers is",a*b);
if(choice=='/'):
    print("Division of the two numbers is",a/b);
else:
    print("Operation not applicable----!")