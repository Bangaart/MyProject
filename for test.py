def fib(n):
    a,b,result= 10, 20 , 0
    if n == 1:
        print(a)
    if n == 2:
        print(b)
    for i in range(n-2):
       res = a+b
       a,b = b, res
    print(result)

fib(6)
print("Should be in adds branch")

