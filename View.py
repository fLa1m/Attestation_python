import json

def screen(note_list: list):
    text = str()
    for i in note_list:
        text += json.dumps(i, ensure_ascii=False)
        text += "\n"
    print(text)

def __select_menu(commands: list) -> int:
    select = input(">>> ")
    try:
        select = int(select)
        if select < 0 or len(commands) < select:
            raise Exception("Такой команды нет.")
    except ValueError as ex:
        print("Повторите ввод.")
        return __select_menu(commands)
    except Exception as ex:
        print(ex)
        return __select_menu(commands)
    else:
        return select
    
def menu():
    commands = [
        "Показать все заметки",
        "Поиск по дате",
        "Поиск по тексту",
        "Добавить заметку",
        "Изменить заметку",
        "Удалить заметку",
        "Выход"
    ]
    print("Укажите номер команды: ")
    print("\n".join(f"{k}. {v}" for k, v in enumerate(commands, 1)))
    return __select_menu(commands)