#1
def numbers_product(start, end, step):
    numbers_list = []
    product = 1
    current_number = start
    while current_number < end:
        numbers_list.append(current_number)
        if current_number % 3 == 0:
            product *= current_number
        current_number += step
    return product
start = 1
end = 20
step = 2
result = numbers_product(start, end, step)
print(f"Product of multiples of 3: {result}")

#2
def perform_operations(result):
    second_number = int(input("Enter the second number: "))

    #mathematical operations
    addition = result + second_number
    subtraction = result - second_number
    multiplication = result * second_number

    if second_number != 0:
        division = result / second_number
    else:
        division = "Cannot divide by zero"
    
    print(f"Result of addition: {addition}")
    print(f"Result of subtraction: {subtraction}")
    print(f"Result of multiplication: {multiplication}")
    print(f"Result of division: {division}")
   

start = 1
end = 20
step = 2
result = numbers_product(start, end, step)
perform_operations(result)

#3
def hashtag_generator():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    hashtag = ''.join(word.capitalize() for word in words)
    hashtag = '#' + hashtag
    return hashtag
result = hashtag_generator()
print(result)

#4
def num_divisors(number):
    divisors = []

    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

number = int(input("Enter a number: "))
result = num_divisors(number)
print(result)

#5
def manual_split(word, start, end, step):
    result = ""
    for i in range(start, end, step):
         result += word[i]

    return result

user_word = input("Enter a word: ")
start = int(input("Enter the start index: "))
end = int(input("Enter the end index: "))
step = int(input("Enter the step size: "))
result = manual_split(user_word, start, end, step)
print(result)

#codewars
#1
def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))


#2
def is_square(n): 
    if n < 0:
     return False
    square_root = n ** 0.5
    return square_root.is_integer()

#3
def xo(s):
    count_x = s.lower().count('x')
    count_o = s.lower().count('o')
    return count_x == count_o
    




    