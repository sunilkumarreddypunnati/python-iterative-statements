'''Task 9: Prime Number Check 
👉 Take a number as input and 
check if it is prime or not using a loop.'''
n=int(input("enter number:"))
if n<=1:
    print(n,"this is not prime")
else:
    for i in range (2,n):
        if n%i==0:
            print(n,"this is not prime")
            break
    else:
        print(n,"this is prime")