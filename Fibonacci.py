fib1 = 0
fib2 = 1
t1 = int(input("Digite qual número da sequência de Fibonacci que você gostaria de descobrir: "))
cont = 0
total = 0
if t1 > 1:
    while cont != t1:
        total = fib1 + fib2
        fib1 = fib2
        fib2 = total
        cont = cont +1
    print(total)
elif t1 == 1:
    print(fib2)
else:
    print(fib1)
