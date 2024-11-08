Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n = 13 # enter your favorite number here!
step = 0

print("Step","\t","Number") #We use '\t' to make a tab-separated table

while n!=1:
    print(step, "\t", n)
    
    #We can check whether our number is even using the modulus operator
    if n%2 ==0: 
        n = n/2
    else:
        n = 3*n+1
    step = step+1 
#The following else command tells us what to do when the while loop is finished.
else:
    print("We get 1 at Step",step)
