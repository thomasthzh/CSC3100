n, m = map(int, input().split())
edges = []
total = 0
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))
    total += w

parent = list(range(n))
size = [1] * n

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

edges.sort()
mst = 0
used = 0
for w, u, v in edges:
    ru = find(u); rv = find(v)
    if ru == rv:
        continue
    if size[ru] < size[rv]:
        ru, rv = rv, ru
    parent[rv] = ru
    size[ru] += size[rv]
    mst += w
    used += 1
    if used == n - 1:
        break

if used == n - 1:
    print(total - mst)
else:
    print("IMPOSSIBLE")