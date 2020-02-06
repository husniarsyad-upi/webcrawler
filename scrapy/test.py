arr = [1,2,3,4,5]

total1 = 0
total2 = 0
count = 0
low = 0
hi = 0

for x in arr:
    total1 += x
    total2 += x

    if count == 0:
        low = x
        hi = x
    else:
        if low > x:
            low = x
        if hi < x:
            hi = x

    count += 1

print((total1-hi),(total2-low))
