import time

start_time = time.perf_counter()


def cantor(n : int) -> str:
    def numf(m):
        a = []
        for i in range(1, m+1):
            a.append(str(i))
        return(a)


    def numb(m):
        a =[]
        for i in range(1,m+1):
            b = m - i
            a.append(str(b))
            if '0' in a:
                a.remove('0')
        return(a)
    
    lis = []
    for i in range(n):
        if i%2 != 0:
            d = numf(i) + numb(i)
            lis += d

    kis = []
    for j in range(n):
        if j%2 == 0:
            h = numf(j) + numb(j)
            kis += h

    g = []
    for k,l in zip(lis,kis):
        o = k + "/" + l
        g.append(o)

    return g[n-1]

print(cantor(2500))



for i in range(1000000):
    pass

end_time = time.perf_counter()

execution_time = end_time - start_time
print(f"Execution time: {execution_time:.6f} seconds")