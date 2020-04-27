import csv, json


def books_():
    with open('books.csv') as file:
        reader = csv.reader(file)
        for line in reader:
            yield {"title": line[0], "author": line[1], "height": line[3]}


book = books_()
next(book)

final_list = []
with open('users.json') as users:
    users_list = json.load(users)
    for user in users_list:
        user_to_add = {}
        user_to_add["name"] = user["name"]
        user_to_add["gender"] = user["gender"]
        user_to_add["address"] = user["address"]
        book_to_add = []
        book_to_add.append(next(book))
        user_to_add["books"] = book_to_add
        final_list.append(user_to_add)

with open('final_list.json', 'w') as f:
    json.dump(final_list, f, indent=4)

print('\n---finished---')
