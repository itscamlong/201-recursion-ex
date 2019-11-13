def factorial(n):
    # Prevent negative numbers... because duh
    if n < 0:
        print("Can't do negative numbers!")
        return 0
    
    # It's the base case!
    elif n == 1:
        return 1
    
    # Ladies and gentleman... recursion
    else:
        answer = n * factorial(n-1)
        return answer

if __name__ == '__main__':
    print(factorial(15))