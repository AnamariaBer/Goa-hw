#Create a dictionary for books with their names and prices
books = {
    "Book1": 200,
    "Book2": 251,
    "Book3": 17,
    "Book4": 39,
    "Book5": 63,
    "Book6": 120,
    "Book7": 85,
    "Book8": 35,
    "Book9": 40,
    "Book10": 25
}

#Create an empty dictionary for discoynted prices
discounted_prices = {}

#Define variables of discounts
discount1 = 10
discount2 = 20

#create a for loop which itirates over key value pairs in the dictionary and applies discounts
for book, price in books.items():
    if int(book[4:]) <= 5: 
        discounted_prices[book] = price - price * discount1 / 100  #applies a 10% discount to the first 5 books
    else:
        discounted_prices[book] = price - price * discount2 / 100  #applies a 20% discount to the rest of the books

#Print discounted prices for all books
for book, discounted_price in discounted_prices.items():
    print(f"{book} = {discounted_price}")