#  problem - 1

age = input("Enter your age: ")
# age = int(input("Enter your age: "))

print("type of input age: ", type(age))
age_in_int = int(age)

if age_in_int < 13: 
    print("child")
elif(age_in_int >= 13) and (age_in_int < 19):
    print("teenager")
elif(age_in_int >= 19) and (age_in_int < 59):
    print("adult")
else:
    print("senior")

