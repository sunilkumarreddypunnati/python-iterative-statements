'''Task 5: Reverse a Number
👉 Take a number and print its reverse.
Example: Input 123 → Output 321'''
n=(int(input("please enter number:")))
original=n
reverse =0
while n>0:
    digit = n % 10         # get last digit
    reverse = reverse * 10 + digit
    n = n // 10   
print("reverse of", original, "is",reverse)
