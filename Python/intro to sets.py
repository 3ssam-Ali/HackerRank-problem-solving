
def average(array):
    # your code goes here
    s=set(array)
    av=round(sum(s)/len(s),3)
    return av
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

