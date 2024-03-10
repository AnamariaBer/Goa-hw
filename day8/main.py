required_weight = 50
required_height = 170

user_weight = int(input("Enter your weight: "))
user_height = int(input("Enter your height: "))

#checking the weight
if user_weight == required_weight:
    print("Your weight equals the required weight.")
else:
    print("Your weight does not equal the required weight.")

if user_weight > required_weight:
    print("Your weight is greater than the required weight.")
elif user_weight < required_weight:
    print("Your weight is less than the required weight.")

#checking the height
if user_height == required_height:
    print("Your height equals the required height.")
else:
    print("Your height does not equal the required height.")

if user_height > required_height:
    print("Your height is greater than the required height.")
elif user_height < required_height:
    print("Your height is less than the required height.")

