""" 1)შექმენით ლისტი სადაც ჩამოწერილიქნება თამაშის სახელები და 
შემდგომ თამაშებს ვანაცვლებთ სოლოლერნით , w3 , codewars - ებით და ასეშემდეგ."""

games_list = ["Valorant", "League of Legends", "Fortnite"]

print(f"Original list: {games_list}")

games_list[0] = "Sololearn"
games_list[1] = "w3schools"
games_list[2] = "Codewars"

print(f"Modified list: {games_list}")

"""2)შექმენით 5 ინფუთი და ამ ინფუთებით შეადგინეთ სია, 
შემდეგ გამოიტანეთ ამ სიიდან ლუწი რიცხვები, ისე რომ ლოგიკამ ყველა შემთხვევაში იმუშაოს"""

input_list = []
for i in range(5):
  num = int(input("Enter a number: "))
  input_list.append(num)
    

for num in input_list:
  if num % 2 == 0:
    print(num)


