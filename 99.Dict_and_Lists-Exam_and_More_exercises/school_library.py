def add_book(book_list, name_of_book):
    if name_of_book not in book_list:
        book_list.insert(0, name_of_book)
    return  book_list


def take_book(book_list, name_of_book):
    if name_of_book in book_list:
        book_list.remove(name_of_book)
    return book_list


def swap_books(book_list, name_of_book, name_of_second_book):
    if name_of_book in book_list and name_of_second_book in book_list:
        first_book_index = book_list.index(name_of_book)
        second_book_index = book_list.index(name_of_second_book)
        book_list[first_book_index], book_list[second_book_index] = book_list[second_book_index], book_list[first_book_index]
    return book_list


def insert_books(book_list, name_of_book):
    book_list.append(name_of_book)
    return book_list


book_list = input().split('&')
line = input()

while not line == 'Done':
    tokens = line.split(' | ')
    command = tokens[0]
    name_of_book = str(tokens[1])

    if command == 'Add Book':
        book_list = add_book(book_list, name_of_book)
    elif command == 'Take Book':
        book_list = take_book(book_list, name_of_book)
    elif command == 'Swap Books':
        name_of_second_book = tokens[2]
        book_list = swap_books(book_list, name_of_book, name_of_second_book)
    elif command == 'Insert Book':
        book_list = insert_books(book_list, name_of_book)
    elif command == 'Check Book':
        index = int(name_of_book)
        if len(book_list) > index:
            print(book_list[index])
        else:
            pass


    line = input()
print(*book_list, sep=', ')