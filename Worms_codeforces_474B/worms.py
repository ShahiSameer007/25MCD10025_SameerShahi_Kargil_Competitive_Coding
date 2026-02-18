import bisect

n = int(input())
a = list(map(int, input().split()))

for i in range(1, n):
    a[i] += a[i-1]

m = int(input())
queries = list(map(int, input().split()))

for x in queries:
    print(bisect.bisect_left(a, x) + 1)
