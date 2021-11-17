def merge_the_tools(string, k):
    # your code goes here
    t=[string[i-k:i] for i in range(k,len(string)+1,k)]
    u=[''.join(dict.fromkeys(s)) for s in t]
    print(*u,sep='\n')

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)