"""დაწერეთ ალგორითმი რომელიც დაბეჭდავს დადებითია,
 უარყოფითი თუ ნულის ტოლი მომხმარებლის მიერ შემოტანილი რიცხვი."""

num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
elif num == 0:
    print("0")

"""დაწერეთ ალგორითმი რომელიც მომხმარებელს შეთავაზებს ორ ოპერაციას: კილომეტრი - მილი, მილი - კილომეტრი. 
მომხმარებელმა უნდა აირჩიოს ერთ-ერთი მათგანი, ხოლო შემდეგ შეეკითხეთ რიცხვითი მნიშვნელობა, 
რომელზეც მოახდენთ მუშაობას და საბოლოოდ დაუბეჭდეთ უკვე გადაყვანილი მნიშვნელობა. 
თუ მომხმარებელი სწორად არ აირჩევს ოპერაციას, დაბეჭდეთ "Wrong decision"."""

print("Choose an operation: 1. Kilometer to Mile  2. Mile to Kilometer ")
choice = float(input("Enter 1 or 2: "))

def kilometer_to_mile(km):
    return km * 0.621371

def mile_to_kilometer(mile):
    return mile * 1.60934

if choice == 1:
    km = float(input("Enter distance in kilometers: "))
    converted = kilometer_to_mile(km)
    print(f"{km} kilometers is equal to {converted} miles.")
elif choice == 2:
    mile = float(input("Enter distance in miles: "))
    converted = mile_to_kilometer(mile)
    print(f"{mile} miles is equal to {converted} kilometers.")
else:
    print("Wrong decision. Please choose 1 or 2.")

"""შექმენით რეგისტრაციის ალგორითმი. მომხმარებელს შეეკითხეთ სახელი, გვარი, ასაკი და მეილი,
 საბოლოოდ კი ერთ წინადადებაში გამოიტანეთ მიღებული ინფორმაცია."""

name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
email = input("Enter your email address: ")

print(f"Your name is {name}, your surname is {surname}"
      f"You are {age} years old, and your email address is {email}.")

"""მომხმარებელს სამჯერ შეეკითხეთ რიცხვითი მნიშვნელობა და დაბეჭდეთ მათი საშუალო არითმეტიკული."""

def num_input():
  return int(input("Enter a number: "))

num1 = num_input()
num2 = num_input()
num3 = num_input()

sum = num1 + num2 + num3
average = sum / 3
print(f"The arithmetic average is {average}")

"""მომხმარებელს შეეკითხეთ 1-იდან 9-ის ჩათვლით რომელიმე რიცხვი. 
შემდეგ გამოიყენეთ for ციკლი და გამოიტანეთ ამ რიცხვის ჯერადები 1-იდან 50-მდე დიაპაზონში."""

num = int(input("Enter a number from 1 to 9:"))

for i in range(1, 51):
    if i % num == 0:
        print(i)

"""მომხმარებელს შემოატანინეთ ორი რიცხვი. შემდეგ მათ შორის უმცირესი for ციკლში საწყის,
 ხოლო უდიდესი საბოლოო მნიშვნელობად გამოიყენეთ. 
 ციკლში იტერაცია მოახდინეთ ერთით და გამოიტანეთ საიტერაციო ცვლადის მესამე ხარისხი (კუბი).
"""
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

smallest = min(num1, num2)
largest = max(num1, num2)

for i in range(int(smallest), int(largest)):
    print(i**3)

"""მომხმარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ მისი ციფრთა ჯამი."""


def sum_of_digits(number):
    number_str = str(number)
    total = 0

    for digit in number_str:
        total += int(digit)
    return total


number = int(input("Enter a number: "))


result = sum_of_digits(number)
print(f"The sum of digits in {number} is: {result}")

"""დაწერეთ პროგრამა, რომელიც იღებს მომხმარებლისგან მთელ რიცხვს და 
დაბეჭდავს მის გამრავლების ცხრილს 10-ის ჩათვლით. მაგ: x, x2, x3 ... x*10."""


number = int(input("Enter a number: "))

for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")

"""შექმენით კალკულატორი, სადაც გექნებათ ოთხი ოპერაცია: + - / და გამრავლება (ფიფქი არ იწერება).
 მომხმარებელს შეეკითხებით ორ რიცხვს, შემდეგ სასურველ ოპერაციას და 
 დაუბეჭდავთ გამოთვლილ მნიშვნელობას."""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
choice = input("Choose your desired operation: +, -, *, or /: ")

if choice == '+':
    print(num1 + num2)
elif choice == '-':
    print(num1 - num2)
elif choice == '*':
    print(num1 * num2)
elif choice == '/':
   print(num1 / num2)

"""დაწერეთ პროგრამა, რომელიც იღებს სთრინგს, შემდეგ მომხმარებელს ეკითხება თუ რამდენჯერ განმეორდეს
 და for ციკლის გამოყენებით დაბეჭდეთ ის."""

input_string = input("Enter a string: ")

repeat_times = int(input("How many times do you want to repeat the string? "))

for i in range(repeat_times):
    print(input_string)

"""დაწერეთ პროგრამა, რომელიც გამოთვლის სხეულის მასის ინდექსს (BMI), 
მომხმარებლისგან მიღებული წონის (კილოგრამებში) და სიმაღლის (მეტრებში) გათვალისწინებით."""

def calculate_bmi(weight, height):
    return weight / (height ** 2)

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi}")

"""დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს რიცხვი 1-დან 5-ის ჩათვლით. 
თუ რიცხვი არის 1-ზე ნაკლები ან 5-ზე მეტი, 
დაბეჭდეთ "Invalid input". თუ რიცხვი 1-დან 5-ის ჩათვლითაა, დაბეჭდეთ "Valid input"."""

number = int(input("Enter a number from 1 to 5: "))

if 1 <= number <= 5:
    print("Valid input")
else:
    print("Invalid input")
