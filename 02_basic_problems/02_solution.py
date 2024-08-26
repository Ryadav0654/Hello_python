age = int(input("Enter your age: "))
day = input("Enter day: ")

# if age > 18:
#     if day == 'wednesday':
#         print("ticket price is: $", 10)
#     else:
#         print("ticket price is: $", 12)
# else:
#     if day == 'wednesday':
#         print("ticket price is: $", 6)
#     else:
#         print("ticket price is: $", 8)
        
        
# short form 

price = 12 if age >= 18 else 8

if day == 'wednesday':
    # price = price - 2
    price -= 2
    
print("ticket price is $", price)

    