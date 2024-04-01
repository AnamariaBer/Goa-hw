"""შექმენით სია სადაც შეინახავთ თქვენთვის საყვარელ ფილბეს და დაბეჭდეთ მთლიანი სია/ კონკრეტული ფილმი"""

favorite_movies = [
    "Interstellar",
    "The Godfather",
    "Drive",
    "Donnie Darko",
    "Blade runner 2049",
    "Se7en",
    "Nightcrawler",
    "Inception",
    "Fight Club",
    "Whiplash",
    "Requiem of a dream",
    "Eternal sunshine of the spotless mind"
]

print(f"My favorite movie is {favorite_movies[9]}.")

"""შექმენით 2 სია და გააერთიანეთ ისინი"""

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8, 9, 10]
merged_list = list1 + list2
print(merged_list)

"""შექმენით სტრინგი მაგ. თქვენი სახელი, და გამოიტანეთ სახელის პირველი და ბოლო სიმბოლო"""
name = "Anamaria"
print(name[0] + name[7])

""" შექმენით სია და სტრინგი ხოლო შემდეგ დაბეჭდეთ len ფუნქციის გამოყენებით მათი ზომა"""

my_list = [1, 2, 3]
my_string = "Hello, World!"

print(f"The size of the list: {len(my_list)}\nThe size of the string: {len(my_string)}")

"""შეცვალეთ სიიდან რომელიმე მნიშვნელობა"""

print(f"Original list: {my_list}")
my_list[0] = 0
print(f"Modified list: {my_list}")

"""შექმენით რიცხვების სია სადაც 10 რიცხვს შეიტანთ, 
გამოიტანეთ პირელ ინდექსა და ბოლო ინდექსზე მყოფი ელემენტების ჯამი"""

numbers_list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(f"The sum is {numbers_list[0] + numbers_list[9]}")

