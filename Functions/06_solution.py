def sum_all(*args):
    
    print("args: ", args) # it gives tuple
    print(type(args))
    print("*args: ", *args)
    return sum(args)


print("all sum: ", sum_all(1, 3, 5, 6 ,6 , 7))

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

        
print_kwargs(name="shaktiman", power="lazer")
print_kwargs(name="Ironman", power="lazer")
print_kwargs(name="hero")