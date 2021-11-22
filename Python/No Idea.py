input()
li=input().split()
a=set(input().split())
b=set(input().split())
h=0
for i in li:
    if i in a: h+=1
    elif i in b : h-=1
print(h)