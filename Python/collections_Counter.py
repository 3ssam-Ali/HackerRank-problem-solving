from collections import Counter
n=input()
stock=Counter(input().split())
profit=0
for i in range(int(input())):
    s,p=input().split()
    if stock[s]:
        stock[s]-=1
        profit+=int(p)
print(profit)

