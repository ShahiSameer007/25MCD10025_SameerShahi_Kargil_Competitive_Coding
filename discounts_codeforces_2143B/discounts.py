t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    prod = list(map(int, input().split()))
    disc = list(map(int, input().split()))

    prod.sort()
    disc.sort()

    total = sum(prod)

    right = n - 1 

    for x in disc:
        if right - x + 1 < 0:
            break
        free_index = right - x + 1
        total -= prod[free_index]

        right -= x 

    print(total)
