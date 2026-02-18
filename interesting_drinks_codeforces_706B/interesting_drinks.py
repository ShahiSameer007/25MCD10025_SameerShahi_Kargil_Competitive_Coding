import bisect

n = int(input())
x = list(map(int, input().split()))
q = int(input())

m = []
for _ in range(q):
    m.append(int(input()))

x.sort()

for i in range(len(m)):
    count = bisect.bisect_right(x, m[i])
    print(count)
