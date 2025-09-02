'''task 6: Count Digits in a Number 
👉 Input: 98765 → Output: 5 digits.'''
n=int(input("enter number:"))
num=n
count=0
while n>0:
    n=n//10
    count+=1
print("count of digits in",num,"is",count)