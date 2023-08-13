import Notes
import FileManagment as fm
import pandas as pd

def __new_note():
    note = Notes.Notes()
    note.set_title(input("Введите заголовок заметки: "))
    note.set_note_body(input("Введите текст заметки: "))
    return note

def __search(note: dict, find):
    for v in note.values():
        if find in v:
            return note

def add_note(note_list: list):
    note_list.append(__new_note().to_dict())
    fm.save_file(note_list)

def find_note(note_list: list):
    print("Введите данные для поиска: ")
    val = input(">>> ")
    result = list(filter(lambda x: __search(x,val), note_list))
    return result

def data_filter(note_list: list):
    print("Введите дату в формате dd.mm.yyyy: ")
    val = input(">>> ")
    df = pd.DataFrame(note_list)
    result = df.loc[df["data"].str.contains(val)]
    return result.to_dict('records')

def change_note(note_list: list):
    # val = find_note(note_list)
    # View.screen(val)
    id = input("Введите id заметки: ")
    for notes in note_list:
        if id == notes["id"]:
            note = __new_note()
            notes["title"] = note.get_title()
            notes["body"] = note.get_note_body()
            notes["data"] = note.get_last_change_date()
            print("Заметка изменена.")
    fm.save_file(note_list)

def delete_note(note_list: list):
    # val = find_note(note_list)
    # View.screen(val)
    id = input("Введите id заметки: ")
    for notes in note_list:
        if id == notes["id"]:
            note_list.remove(notes)
            print("Заметка удалена.")
    fm.save_file(note_list)

