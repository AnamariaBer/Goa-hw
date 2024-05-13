#1
def twice_as_old(dad_years_old, son_years_old):
    years_ago = abs(2 * son_years_old - dad_years_old)
    return years_ago

#2 
def sum_str(a, b):
    if a == "":
        a = "0"
    if b == "":
        b = "0"
    sum_result = int(a) + int(b)
    return str(sum_result)

#3
def reverse_seq(n):
    if n <= 0:
        return []
    else:
        return list(range(n, 0, -1))
    
#4
def no_space(x):
    #your code here
    return x.replace(" ", "")

#5 
def abbrev_name(name):
    first_name, last_name = name.split()
    first_initial = first_name[0].upper()
    last_initial = last_name[0].upper()
    abr_name = f"{first_initial}.{last_initial}"
    return abr_name

#6
def factorial(n):
    result = 1
    for num in range(n, 0, -1):
       result *= num
    return result

#7
def divisors(integer):
    result = []
    for x in range(2, integer):
        if integer % x == 0:
            result.append(x)
    if len(result) == 0:
        return f"{integer} is prime"
    return result

#8
def divisors(n):
    divisors = []
    for x in range(1, n + 1):
        if n % x == 0:
            divisors.append(x)
    return len(divisors)

#9
def capitals(word):
    capital_indices = []
    for index, char in enumerate(word):
        if char.isupper():
            capital_indices.append(index)
    return capital_indices

#10
def solve(s):
    uppercase_count = sum(1 for char in s if char.isupper())
    lowercase_count = sum(1 for char in s if char.islower())
    if lowercase_count >= uppercase_count:
        return s.lower()
    else:
        return s.upper()
    