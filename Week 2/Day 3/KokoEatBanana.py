# Koko Eating Bananas

import math

piles = [30, 11, 23, 4, 20]
h = 6
low = 1
high = max(piles)
ans = high

while low <= high:
    mid = (low + high) // 2

    hours = 0
    for banana in piles:
        hours += math.ceil(banana / mid)

    if hours <= h:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print(ans)