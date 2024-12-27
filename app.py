from flask import Flask, abort, redirect, render_template, request, url_for
import sqlite3

"""Global Variables"""
app = Flask(__name__)

CATEGORIES = ("school", "work", "hobbies", "other")


"""Functions"""
# create table SQL
def create_table():
    with sqlite3.connect('notebook.db') as db:
        db.execute('''CREATE TABLE IF NOT EXISTS notes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT,
                title TEXT,
                content TEXT,
                date TEXT)''')
        db.commit()

# view all notes
def all_notes():
    with sqlite3.connect('notebook.db') as db:
        notes = db.execute('SELECT * FROM notes').fetchall()
        return notes

# view all notes of the selected category
def all_notes_for_selected_category(category):
    with sqlite3.connect('notebook.db') as db:
        notes = db.execute('SELECT * FROM notes WHERE category = ?', (category,)).fetchall()
        return notes


# Insert new note function SQL
def insert_note(category, title, content, date):
    with sqlite3.connect('notebook.db') as db:
        db.execute('INSERT INTO notes (category, title, content, date) VALUES (?, ?, ?, ?)',
                   (category, title, content, date))
        db.commit()

# View one note function by title search
def view_note(id):
    with sqlite3.connect('notebook.db') as db:
        note = db.execute('SELECT * FROM notes WHERE id = ?', (id,)).fetchone()
        return note

# Delete note function SQL
def delete_note(id):
    with sqlite3.connect('notebook.db') as db:
        db.execute('DELETE FROM notes WHERE id = ?', (id,))
        db.commit()


# Edit note function SQL
def edit_note(category, title, content, date, id):
    with sqlite3.connect('notebook.db') as db:
        db.execute('UPDATE notes SET category=?, title=?, content=?, date=? WHERE id=?',
                   (category, title, content, date, id))
        db.commit()


"""ENDPOINTS"""
# Display all notes on index page
@app.route("/")
def index():
    notes = all_notes()
    return render_template('index.html', notes=notes)

# Display notes for chosen category
@app.route("/note/<category>")
def category(category):
    if not category in CATEGORIES:
        abort(404)

    notes = all_notes_for_selected_category(category)
    return render_template(f'{category}.html', notes=notes)

# Create New Note
@app.route('/note/new', methods=['GET', 'POST'])
def new_note():
    if request.method == 'POST':
        category = request.form.get("category")
        title = request.form.get("title")
        content = request.form.get("content")
        date = request.form.get("date")
        insert_note(category, title, content, date)

        return redirect(url_for('index'))
    return render_template('new_note.html')

# Edit Note
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        category = request.form.get("category")
        title = request.form.get("title")
        content = request.form.get("content")
        date = request.form.get("date")
        # id = request.form.get("id") id is already passed in. If this is implemented it will overide the id with none because the edit html doesnt pass any id.
        # therefore none will be passed and the updae won't happen unless there is an id of none.
        edit_note(category, title, content, date, id)
        return redirect(url_for('index'))
    note = view_note(id)
    if note == None:
        abort(404)

    return render_template('edit.html', note=note)

# Delete Note
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    if request.method == 'POST':
        delete_note(id)

        return redirect(url_for('index'))
    note = view_note(id)
    return render_template('delete.html', note=note)


"""MAIN"""

def main():
    create_table()
main()

if __name__ == "__main__":
    app.run(debug=True)
