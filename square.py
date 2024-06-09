
x=int(input("Enter a number: "))
n=0
while x>0:
    a = x%10
    x =x - a
    x = x/10
    print(int(a),end="")
    n = n + 1