#1 
def litres(time):
    if time <= 0:
        return 0
    water_per_hour = 0.5
    total_water = water_per_hour * time
    return int(total_water)
#2
def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    else:
        return n * m
#3 
def grow(arr):
    result = 1
    for i in arr:
        result *= i
    return result
#4
def fake_bin(x):
    result = ''
    for digit in x:
        if int(digit) < 5:
            result += '0'
        else:
            result += '1'
    return result
#5 
def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    return [i * x for i in range(1, n + 1)]
#6
def to_jaden_case(string):
    # ...
    words = string.split()
    jaden_case_words = [word.capitalize() for word in words]
    return ' '.join(jaden_case_words)
#7
def accum(st):
    result = ''
    for i, char in enumerate(st):
        result += char.upper() + char.lower() * i + '-'
    return result[:-1]
#8
def remove_smallest(numbers):
    if not numbers:
      return []
    min_value = min(numbers)
    min_index = numbers.index(min_value)
    return numbers[:min_index] + numbers[min_index+1:]
#9
def solution(number):
    if number < 0:
        return 0
    result = 0
    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            result += num  
    
    return result
#10
def likes(names):
    if not names:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"