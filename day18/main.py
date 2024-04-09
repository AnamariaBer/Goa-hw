"""მომხმარებელს შემოატანინეთ ხუთი რიცხვი და ყველა შეიტანეთ სიაში. 
თქვენი დავალებაა,რომ დაბეჭდოთ ამ სიის ჯამი, არ გამოიყენოთ sum მეთოდი."""

numbers = []
for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)

total = 0
for num in numbers:
    total += num

print(f"The sum of the numbers is: {total}")

"""სიაში შეიტანეთ თქვენთვის სასურველი 10 რიცხვი. დაბეჭდეთ ამ სიაში არსებული 
ყველაზე დიდი რიცხვი, მინიშნება: გამოიყენეთ for ციკლი. 
არ გამოიყენოთ max მეთოდი."""

numbers = []
for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

largest = numbers[0]  
for num in numbers:
    if num > largest:
        largest = num


print(f"The largest number in the list is: {largest}")

"""სიაში შეიტანეთ 30-იდან 50-ის ჩათვლით არსებული ყველა რიცხვი. შემდეგ
 დაითვალეთ ამ სიაში არსებული კენტი რიცხვები და დაბეჭდეთ მათი რაოდენობა."""

numbers = list(range(30, 51))

odd_numbers = []
for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)

print(f"The odd numbers are: {odd_numbers}")

"""სიაში შეიტანეთ 10-იდან 50-ის ჩათვლით არსებული 4-ის ჯერადი რიცხვები. 
შემდეგ შეაბრუნეთ ეს სია და დაბეჭდეთ ის, test case: [1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1]"""
        
multiples_of_4 = list(range(10, 51, 4))

multiples_of_4.reverse()
print(f"the reversed list is: {multiples_of_4}")

