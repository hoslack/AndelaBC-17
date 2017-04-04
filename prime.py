def primenumber(n):

    for num in range(0, n+1):
        if all(num % i != 0 for i in range(2, num)):
            print num

