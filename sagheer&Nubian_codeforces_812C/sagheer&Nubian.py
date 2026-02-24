import sys
n,S = map(int,sys.stdin.readline().split())
base_cost = list(map(int,sys.stdin.readline().split()))

def can(k):
    sp = [base_cost[i] + (i+1) * k for i in range(n)]
    sp.sort()
    return sum(sp[:k])

left, right = 0,n
best_k = 0
best_cost = 0

while left <= right:
    mid = (left + right) // 2
    cost = can(mid)

    if cost <= S:
        best_k = mid
        best_cost = cost
        left = mid + 1
    else:
        right = mid - 1

print(best_k,best_cost)