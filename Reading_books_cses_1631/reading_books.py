n = int(input())
time = list(map(int,input().split()))
time.sort()
diff = time[-1] - sum(time[:-1])
if diff > 0:
    waiting_time = sum(time) + diff
else:
    waiting_time = sum(time)
print(waiting_time)