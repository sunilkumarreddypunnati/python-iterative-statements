'''Task 4: Factorial of a Number
👉 Take a number and find its factorial using a loop.
Example: 5! = 120.'''
n=int(input("enter number:"))
fact=1
for i in range(1,n+1):
    fact*=i
print("factorial of",n,"is", fact)