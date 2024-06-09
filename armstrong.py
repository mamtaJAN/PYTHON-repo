    
n = int (input ("Enter a number="))
sum=0
temp=n
n1=len(str(n))
while temp > 0:
        rem = temp %10
        sum=sum+rem**n1
        temp //=10
if n == sum:
    print("armstrong number")
else:
      print("not armstrong")
            
       