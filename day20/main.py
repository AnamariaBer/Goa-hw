#Even or Odd
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
#Convert a Number to a String!
def number_to_string(num):
    string = str(num)
    return string

#Opposite number
def opposite(number):
    return -number

#Return Negative
def make_negative( number ):
    if number > 0:
        return -number
    else:
        return number

#Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(bool):
    return "Yes" if bool else "No"

#Sum of positive
def positive_sum(arr):
    total = 0
    for num in arr:
        if num > 0:
            total += num
    return total

#Remove First and Last Character
def remove_char(s):
  #your code here
  return s[1:-1]

#Square(n) Sum
def square_sum(numbers):
     return sum(x**2 for x in numbers)
    #your code here

#Remove String Spaces
def no_space(x):
    return x.replace(" ", "")