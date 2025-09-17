def generate_series(n):
    if n%2==0:
        n-=1
    result=[i for i in range(1,2*n,2)]
    return result
n=int(input('enter a number:'))
series=generate_series(n)
print("Output:",', '.join(map(str,series)))
