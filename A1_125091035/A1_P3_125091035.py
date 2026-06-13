import heapq
result = []
heap = []
m, n = map(int, input().split())
def rd(num):
    tmp=[]
    for _ in range(num):
        x , y = map(int, input().split())
        tmp.append((x,y))
    return tmp
P=rd(m)
Q=rd(n)

for i in range(m):
    c, e = P[i]
    d, f = Q[0]
    exp = e + f
    coef = c * d
    heapq.heappush(heap, (exp, coef, i, 0))

while heap:
    exp, coef, p_idx, q_idx = heapq.heappop(heap)
    if result and result[-1][0] == exp:
        result[-1] = (exp, result[-1][1] + coef)
    else:
        result.append([exp, coef])
    if q_idx + 1 < n:
        c, e = P[p_idx]
        d, f = Q[q_idx + 1]
        new_exp = e + f
        new_coef = c * d
        heapq.heappush(heap, (new_exp, new_coef, p_idx, q_idx + 1))

filtered = []
for exp, coef in result:
    if coef != 0:
        filtered.append((exp, coef))

if not filtered:
    print(0)
else:
    filtered.sort()
    print(len(filtered))
    for exp, coef in filtered:
        print(coef, exp)