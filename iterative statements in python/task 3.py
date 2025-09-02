'''Task 3: Sum of Natural Numbers
👉 Take a number n and 
calculate the sum of first n natural numbers using a loop.
Formula check: n*(n+1)/2.'''
n=int(input("enter number:"))
sum_natural=0
for i in range(1,n+1):
    sum_natural+=i
print("sum of first ",n,"natural numbers= ",sum_natural)