def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i
        

for i in even_generator(10):
    print(i)
    
    
    
# recursion 
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

ans = factorial(5)
print(ans)