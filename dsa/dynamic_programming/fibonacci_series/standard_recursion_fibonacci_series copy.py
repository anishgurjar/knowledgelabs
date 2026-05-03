"""
Fibonacci Series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34... 
"""

def fibonacci(n):
    if n == 0 or n == 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)

def main():
    print(fibonacci(9))
    
if __name__ == "__main__":
    main()