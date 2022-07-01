import sys
from ChapterThree.note_book import NoteBook


class Menu:
    def __init__(self):
        self.notebook = NoteBook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }

    def display_menu(self):
        print(""" 
        Notebook Menu 
        1. Show all Notes 
        2. Search Notes 
        3. Add Note 
        4. Modify Note 
        5. Quit 
        """)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid action")

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(f"{note.note_id}: {note.tags}\n{note.memo}")

    def search_notes(self):
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print(self.notebook.notes[0].memo)
        print("Your note has been added.")

    def modify_note(self):
        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(memo, id)
        if tags:
            self.notebook.modify_tags(tags, id)

    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)


if __name__ == '__main__':
    # Menu().run()
# memo_one = 'First Hello, Small Ugly'
# memo_two = 'Second Hello, Small Ugly'
# note_one = Note(memo_one, tags='First')
# note_two = Note(memo_two, tags='Second')
# print(note_one.creation_date, note_two.note_id)
# print(note_two.match('Third'))

# book_one = NoteBook()
# book_one.new_note('hello world', 'first')
# book_one.new_note('hello again', 'second')
# print(book_one.notes[0].tags)
# book_one.modify_memo('hi world', 1)
# print(book_one.notes[0].memo)
# print(book_one.search('hello'))

# book = NoteBook()
# book.new_note('Today is sunny', 'sunny')
# print(book.notes[0].memo)
# book.modify_memo('Today is rainy', 1)
# print(book.notes[0].memo)
    class Demo(object):
        def __init__(self):

            print(object.__doc__)
        pass
    demo = Demo()