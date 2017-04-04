def primenumber(n):
    result = []
    if not isinstance(n, int):
        return TypeError
    elif n <= 0 or n >= 10000:
        return ValueError
    for num in range(0, n+1):
        if all(num % i != 0 for i in range(2, num)):
            result.append(num)
    return result

