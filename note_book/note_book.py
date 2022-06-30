import datetime

note_id = 0
class Note:
    def __init__(self, memo, tags='') -> None:
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global note_id
        note_id += 1
        self.note_id = note_id

    def match(self, filter):
        return filter in self.memo or filter in self.tags


class NoteBook:
    def __init__(self) -> None:
        self.notes = []

    def new_note(self, memo, tags=''):
        self.notes.append(Note(memo, tags))

    def modify_memo(self, memo, note_id):
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, tags, note_id):
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        return False

    def _find_note(self, note_id):
        for note in self.notes:
            if str(note_id) == str(note.note_id):
                return note
        return None

    def search(self, filter):
        return [note for note in self.notes if note.match(filter)]
