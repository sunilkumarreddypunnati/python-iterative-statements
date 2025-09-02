'''Task 8: Sum of Even & Odd Numbers Separately 
👉 Take a number n and 
calculate: Sum of even numbers up to n 
Sum of odd numbers up to n.'''
n=int(input("enter number:"))
sum_even=0
sum_odd=0
for i in range (1,n+1):
    if i%2==0:
        sum_even+=i
    else:
        sum_odd+=i
print("sum of even number upto",n,"=",sum_even)
print("sum of odd number upto",n,"=",sum_odd)
