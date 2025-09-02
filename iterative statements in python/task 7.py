'''Task 7: Fibonacci Series 
👉 Print Fibonacci series up to n terms.
Example: Input 6 → 0, 1, 1, 2, 3, 5.'''
n=int(input("enter number:"))
a,b=0,1
for i in range (0,n):
    a,b=b,a+b
    print(a,end=" ")