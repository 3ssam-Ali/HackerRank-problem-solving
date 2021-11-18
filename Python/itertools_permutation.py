# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s,r=input().split()
print(*sorted([''.join(x) for x in permutations(s,int(r))]),sep='\n')