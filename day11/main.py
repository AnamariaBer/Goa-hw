#task 1
count = 10

while count > 0:
    print(count)  
    count -= 1   

print("Time is up.")

#task 2
sum = 0

while True:
    num = int(input("Enter a number (enter 0 to finish): "))
    

    if num == 0:
        break  
     
    sum += num

print(f"The sum of all numbers is: {sum}")

#task 3

correct_password = 12345678

while True:
    password = int(input("Enter a password: "))

    if password == correct_password:
        break
    else:
        print("Keep guessing")

#task 3
i = 0

while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 2

#task 4
sum = 0

while True: 
  num = int(input("Enter a positive number (enter a negative num to finish): "))
 
  if num < 0:
     break
  sum += num
print(sum)

#task 5
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("It's an even number.")
else:
    print("It's an odd number.")

#task 6
temperature = int(input("Enter the temperature in celsius: "))

if temperature > 30:
    print("Hot (> 30°C)")
elif 20 <= temperature <= 30:
    print("Warm (20-30°C)")
else:
    print("Cold (< 20°C)")

#task 7
score = int(input("Enter the exam score: "))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"
else:
    grade = "F"
print(f"Your grade is {grade}")

#task 8
num = int(input("Enter a number: "))

if num % 2 == 0 and num % 3 == 0:
    print(f"{num} is divisible by 2 and 3")
elif num % 2 == 0:
    print(f"{num} is divisible by 2")
elif num % 3 == 0:
    print(f"{num} isn't divisible by 3")
else:
    print(f"{num} isn't divisible by 2 nor 3")

#task 9
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num2} is greater than {num1}")
else:
    print("Both numbers are equal.")

#task 10
number = 7


while True:
    guess = int(input("Guess the number: "))
        
    
    if guess == number:
        print("You guessed it!")
        break
    else:
        print(f"Try again! The number is not {guess}")

#task 11
while True:
    number = int(input("Enter a number: "))
        
    if number % 2 == 0:
        print("You entered an even number")
        break
    else:
        print("Try again")

#task 12
sum = 0
for number in range(51, 101, 2): 
    print(number)  
    
    
    if number > 75:
        sum += number

print(f"The sum is {sum}")

#task 13
number = int(input("Enter a number: "))
comparison_number = number + 20  # Number greater than the entered number by 20

while number < comparison_number:
    print(number)
    number += 1

#task 14
name = "Anamaria"  
while True:
    guess = input("Guess the name: ")
    
    if guess == name:
        print("You guessed it")
        break
    else:
        print("Try again")

