from collections import defaultdict
d=defaultdict(list)
n,m=map(int,input().split())
for i in range(1,n+1):
    d[input()].append(i)
for i in range(m):
    x=input()
    print(*d[x] if len(d[x])>0 else [-1])