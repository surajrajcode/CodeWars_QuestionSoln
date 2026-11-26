def digital_root(n):
    while n >= 10:
        a = 0  
        for i in str(n):
            a += int(i)
        n = a
    return n
print(digital_root(88))