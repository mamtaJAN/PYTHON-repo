count=0
num=7
while(count<15):
    if (num%2==0 and num%6==0 and num%7==0):
        count+=1
        print(num,"count:",count)
    num+=1

