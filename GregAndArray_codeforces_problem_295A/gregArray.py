n,m,k = map(int,input().split())
arr = list(map(int,input().split()))

ops = []
ops_count = [0 for x in range(m)]
for _ in range(m):
    l,r,d = map(int,input().split())
    ops.append([l,r,d])

queries = []
for _ in range(k):
    x,y = map(int,input().split())
    queries.append([x,y])

for x,y in queries:
    ops_count[x-1] += 1
    if y < m:
        ops_count[y] -= 1

for i in range(m-1):
    ops_count[i+1] += ops_count[i]

for a in range(n-1,0,-1):
    arr[a] -= arr[a-1]

for j in range(m):
    ops[j][2] *= ops_count[j]
    arr[ops[j][0]-1] += ops[j][2]
    if ops[j][1] < n:
        arr[ops[j][1]] -= ops[j][2]

for i in range(n-1):
    arr[i+1] += arr[i]

print(*arr)
