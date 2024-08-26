n = int(input("enter number: "))

even_numbers_sum = 0
for x in range(1, n+1):
    if x % 2 == 0:
        even_numbers_sum += x
        
print(even_numbers_sum)