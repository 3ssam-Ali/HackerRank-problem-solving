n1=int(input())
s1=set(input().split())
n2=int(input())
s2=set(input().split())
li=sorted([int(x) for x in list(s1.symmetric_difference(s2))])
print(*li,sep='\n')

