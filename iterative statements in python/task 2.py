'''Task 2: Multiplication Table
👉 Take a number as input and 
print its multiplication table (1 to 10).
Example: If input is 5 → print 5 × 1 … 5 × 10.'''
n=int(input("enter number:"))
for j in range(1,11):
     print(n,"*",j,"=",n*j)