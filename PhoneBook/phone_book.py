name = ''
phone = ''


def init(person_name, number):
    global name
    global phone
    name = person_name
    phone = number


def person_create(name: str, note: dict, number: str):
    note[name] = [number]
    return note


def add_new_person(name: str, book: dict, number: str):
    book[name[0]] = person_create(name, book, number)
    return book

def person_update(name: str, note: dict, number: str):
    note[name] = number
    return note


def person_delete(name: str, note: dict):
    del note[name]
    return note

def number_append(name: str, number: str, note: dict):
    note[name].append(number)
    return note
