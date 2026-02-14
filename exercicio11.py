n = int(input())
print(1 if n == 0 else __import__('math').factorial(n))
