def generate_odd_series(n):
    list1=[]
    num=1
    for i in range(1,n):
        list1.append(num)
        num+=2
    return list1
n=int(input('enter a number:'))
series=generate_odd_series(n)
print("Output:",', '.join(map(str,series)))
