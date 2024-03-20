"""1) დაწერეთ პროგრამა, რომელიც ეკითხება მომხმარებლის ასაკს და შემდეგ დაბეჭდავს შეტყობინებას ასაკის მიხედვით: using(if-elif-else)
If the age is less than 18, print "You are a minor."
If the age is between 18 and 65, print "You are an adult."
If the age is 65 or older, print "You are a senior citizen."""

age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor")
elif age >= 18 and age < 65:
    print("You are an adult")
elif age >= 65:
    print("You are a senior citizen")

"""2) შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს რიცხვი
 და შემდეგ დაბეჭდოს რიცხვი ლუწია თუ კენტი. გამოიყენეთ ფორ ციკლი, 
 რომ სთხოვოთ მომხმარებელს 5 რიცხვი და შეამოწმეთ ხუთივე რიცხვი.
"""

def check(num):
  if num % 2 == 0:
    return "even"
  else:
    return "odd"

for i in range(5):
  num = int(input("Enter a number: "))
  result = check(num)
  print(f"{num} is {result}")

"""3) დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს ქულები ასოებით (A, B, C, D ან F) და შემდეგ დაბეჭდოს შეტყობინება ასოების მიხედვით: using(if-elif-else)
If the grade is A, print "Excellent!"
If the grade is B, print "Good job!"
If the grade is C, print "You passed."
If the grade is D, print "You can do better."
If the grade is F, print "You failed."""

grade = input("Enter your grade: ")

if grade == 'A':
    print("Excellent!")
elif grade == 'B':
    print("Good job!")
elif grade == 'C':
    print("You passed.")
elif grade == 'D':
    print("You can do better.")
elif grade == 'F':
    print("You failed.")

"""4) დაწერეთ პროგრამა, რომელიც ბეჭდავს რიცხვებს 1-დან 10-მდე while ციკლის გამოყენებით"""
num = 1
while num < 10:
   print(num)
   num += 1

"""5) შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს გამოიცნოს რიცხვი 1-დან 10-მდე. 
გამოიყენეთ while loop, რათა გააგრძელოთ კითხვა, სანამ მომხმარებელი სწორად არ გამოიცნობს"""
import random
correct_num = random.randint(1,10)
while True:
    guess = int(input("Guess the number: "))
    if guess == correct_num:
        print("Congratulations! You guessed it.")
        break
    else:
        print("Try again.")

"""6) დაწერეთ პროგრამა, რომელიც დაბეჭდავს მოცემული რიცხვის 
(მაგ 5) პირველ 10 ჯერადს for loop-ის გამოყენებით."""

for i in range(5, 56, 5):
    print(i)


"""7) შექმენით პროგრამა, რომელიც ბეჭდავს უკუთვლას 10-დან 1-მდე for loop-ის გამოყენებით."""
for i in range(10, 0, -1):
    print(i)
