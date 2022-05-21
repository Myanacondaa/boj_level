n = int(input())

prime = 2
while n != 1:
    if n % prime == 0:
        print(prime)
        n = n/prime

    else:
        prime += 1