a = int(input())
b = int(input())
c = int(input())

if a > b:
    top = a
    low = b
    if c > top:
        top = c
        last = a
    else:
        if c > low:
            last = c
        else:
            low = c
            last = b
else: 
    top = b
    low = a
    if c > top:
        top = c
        last = b
    else:
        if c > low:
            last = c
        else:
            low = c
            last = a
            
print(top)
print(low)
print(last)