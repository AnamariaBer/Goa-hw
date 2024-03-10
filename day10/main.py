#task 1
for i in range(20 + 1):
    print(i)

#task 2
sum = 0 
for i in range(50, 100 + 1):
    sum += i

print(f"the sum of the numbers is {sum}.")

#task 3
for i in range(-10, 10 + 1, 3):
    print(i)

#task 4

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


if num1 < num2:
    smallest = num1
    largest = num2
else:
    smallest = num2
    largest = num1

for i in range(int(smallest), int(largest) + 1, 2):
    print(i)

