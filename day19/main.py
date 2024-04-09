"""უარყოფითი რიცხვების ამოღება: დაწერეთ ალგორითმი, 
რომელიც მიიღებს მთელ რიცხვთა სიას და ამოიღებს ყველა უარყოფით რიცხვს, 
დაბეჭდავს ახალ სიას ამ ელემენტების გარეშე."""

input_list = [2, -3, 5, -7, 11, -13, 0, -1]

positive_list = []

for num in input_list:

    if num >= 0:
        positive_list.append(num)


print(f"List without negative numbers: {positive_list}")

"""საშუალოს პოვნა: დაწერეთ ალგორითმი, 
რომელიც მიიღებს სიას და დააბრუნებს მის საშუალო არითმეტიკულს."""

my_list = [2, 3, 5, 7, 11]
total = sum(my_list)
average = total / len(my_list)
print(f"the arithmetic average of the list is: {average}")

"""სიების შეერთება: დაწერეთ ალგორითმი, რომელიც მიიღებს ორ რიცხვთა სიას, 
გააერთიანებს მათ ერთ სიაში და ამ სახით დაბეჭდავს."""

list1 = [2, 3, 5]
list2 = [7, 11, 13]
merged_list = list1 + list2

print(f"the merged list is: {merged_list}")



