count=0
l=list(map(int,input().split()))
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
           count+=1
print(count)