l=list(input().split())
new=[]
for i in l:
    if l.count(i)%2==0:
        if i not in new:
            new.append(i)
        print(new)
