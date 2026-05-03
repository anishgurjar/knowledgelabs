def fibonacci(n):

    store = {}
    store[0], store[1] = 0, 1

    for i in range(2, n + 1):
        store[i] = store[i-1] + store[i-2]
    
    return store[n]

print(fibonacci(9))