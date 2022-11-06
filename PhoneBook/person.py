import phone_book as pb
import view

t_book = {}
print(t_book)

def writing_down(p_book=t_book):
    name = view.get_name()
    number = view.get_number()
    action = view.what_to_do()
    if action == 'contact':
        if name[0] not in p_book:
            p_book = pb.add_new_person(name, p_book, number)
        p_book = pb.person_create(name, p_book[name[0]], number)
    elif action == 'смена номера':
        p_book = pb.person_update(name, p_book[name[0]], number)
    elif action == 'дополнительный номер':
        p_book = pb.number_append(name, number, p_book[name[0]])
    view.export_book(p_book)