def primenumber(n):
    result = []

    for num in range(0, n+1):
        if all(num % i != 0 for i in range(2, num)):
            result.append(num)
    return result

