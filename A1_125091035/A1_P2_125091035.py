count=0
def merge(arr):
    if(len(arr)==1): 
        yield arr[0]
        return
    global count
    left=list(merge(arr[:len(arr)//2]))
    right=list(merge(arr[len(arr)//2:]))
    i=j=0
    while i<len(left) and j<len(right):
        if(left[i]<=right[j]):
            yield left[i]
            i+=1
        else:
            yield right[j]
            count+=len(left)-i
            j+=1
    yield from left[i:]
    yield from right[j:]

n=input()
arr=list(map(int,input().split()))
result=' '.join(map(str, merge(arr)))
print(count,result,sep='\n')