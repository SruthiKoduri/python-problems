def XOR(n):
    if n%4==1:
        return 1
    if n%4==2:
        return n+1
    if n%4==3:
        return 0
    if n%4==0:
        return n
a=int(input("enter a value: "))
b=int(input("enter b value: "))
c=XOR(a)
d=XOR(b)
M=c^d
print(M)
    
