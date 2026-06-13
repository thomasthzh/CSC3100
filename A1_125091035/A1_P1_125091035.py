import bisect

n, q = map(int, input().split())
arr = list(map(int, input().split()))
inserts = list(map(int, input().split()))

for x in inserts:
    pos = bisect.bisect_right(arr, x)
    print(len(arr) - pos)
    arr.insert(pos, x)

print(' '.join(map(str, arr)))