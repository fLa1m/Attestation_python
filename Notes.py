from datetime import datetime
import uuid

class Notes:
    def __init__(self, id = str(uuid.uuid1())[0:3], title = "текст", note_body = "текст", last_change_date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self._id = id
        self._title = title
        self._note_body = note_body
        self._last_change_date = last_change_date
    

    def get_id(self):
        return self._id
    
    def get_title(self):
        return self._title
    
    def get_note_body(self):
        return self._note_body
    
    def get_last_change_date(self):
        return self._last_change_date
    
    def set_id(self):
        self._id = str(uuid.uuid1())[0:3]

    def set_title(self, title):
        self._title = title

    def set_note_body(self, body):
        self._note_body = body

    def set_last_change_date(self):
        self._last_change_date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def __str__(self):
        return self._id + '; ' + self._title + '; ' + self._note_body + '; ' + self._last_change_date

    def to_dict(self):
        return {"id":self._id, "title":self._title, "body":self._note_body,"data":self._last_change_date}
    