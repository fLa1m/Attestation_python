import NoteManagment as nt
import FileManagment as fm
import View

def start():
    try:
        note_list = fm.load_from_file()
    except FileNotFoundError as er:
        note_list = []
    
    command = View.menu()
    if command == 1:
        View.screen(note_list)
        start()
    elif command == 2:
        View.screen(nt.data_filter(note_list))
        start()
    elif command == 3:
        View.screen(nt.find_note(note_list))
        start()
    elif command == 4:
        nt.add_note(note_list)
        start()
    elif command == 5:
        nt.change_note(note_list)
        start()
    elif command == 6:
        nt.delete_note(note_list)
        start()
    elif command == 7:
        print("Выход.")









