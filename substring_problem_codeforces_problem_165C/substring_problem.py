k = int(input())
s = input()

# Edge case: k = 0
if k == 0:
    count = 0
    curr = 0
    
    for ch in s:
        if ch == '0':
            curr += 1
        else:
            count += curr * (curr + 1) // 2
            curr = 0
    
    count += curr * (curr + 1) // 2
    print(count)
else:
    index_arr = [-1]
    
    for i in range(len(s)):
        if s[i] == "1":
            index_arr.append(i)
    
    index_arr.append(len(s))
    
    count = 0
    
    for i in range(1, len(index_arr) - 1):
        j = i + k - 1
        
        if j < len(index_arr) - 1:
            i_combo = index_arr[i] - index_arr[i-1]
            j_combo = index_arr[j+1] - index_arr[j]
            count += i_combo * j_combo
    
    print(count)
