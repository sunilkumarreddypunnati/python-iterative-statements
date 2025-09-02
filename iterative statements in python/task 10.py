'''Task 10: Pattern Printing (Stars) 
👉 Print the following star pattern using loops: 
* 
** 
*** 
****
*****'''
row=int(input("enter no.of rows:"))
for i in range(1,row+1):
    print("*"*i)