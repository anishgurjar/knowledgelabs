"""
Fibonacci Series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34... 
"""

def fibonacci(n, store):
    if n == 0 or n == 1:
        return n
    
    if n in store:
        return store[n]
    
    else:
        store[n] = fibonacci(n-1, store) + fibonacci(n-2, store)
        return store[n]

def main():
    print(fibonacci(9, {}))
    
if __name__ == "__main__":
    main()