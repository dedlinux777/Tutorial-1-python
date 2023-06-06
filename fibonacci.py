def fibonacci(n):
    f=[0,1]
    for i in range(2, n+1):
        f.append(f[i-2] + f[i-1])
    return f[n]

n=int(input("enter the n value"))
print("f series value at", n, "is", fibonacci(n))