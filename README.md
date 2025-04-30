# Digital Notebook
#### Description:
The Digital Notebook project is a simple web application built using Python and Flask. Useres can create, view, edit, and delete notes. This web-based application leverages SQLite as the database to store user-generated notes. The app supports categorization of notes into predefined categories such as School, Work, Hobbies, and Other. The application features a responsive design and is styled using Bootstrap, making it mobile-friendly.

This project aims to provide users with a clean and intuitive interface to manage their personal notes and organize them based on categories. It also supports CRUD (Create, Read, Update, Delete) operations for note management. The Digital Notebook is an excellent tool for anyone looking to keep track of their ideas with efficient simplicity.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   # Git digital notebook
   git clone https://github.com/TaileyEatherton/digital-notebook.git
   cd digital-notebook
   #(optional)Create pyhton environment and activate it
   python -m venv venv
   source venv/bin/activate
   #Install Flask
   pip install Flask
   #Run application
   flask run

## Features
- **Create Notes**: Users can add new notes by selecting a category, entering a title, content, and date.
- **View Notes**: Notes can be viewed individually or filtered by category.
- **Edit Notes**: Users can modify the content, title, category, and date of their existing notes.
- **Delete Notes**: Notes can be deleted from the application.
- **Category-Based Organization**: Notes are categorized into predefined categories (School, Work, Hobbies, and Other).
- **Responsive Design**: The application is mobile-friendly and adapts to different screen sizes.
- **Bootstrap Styling**: The application uses Bootstrap for layout and design, ensuring a clean and modern look.

## Files and Directories

### 1. **app.py**
This is the main file that contains the logic for the Flask web application. It defines routes for all operations:
- `create_table()`: Initializes the SQLite database and creates the `notes` table if it doesn't exist.
- `all_notes()`: Retrieves all notes from the database.
- `all_notes_for_selected_category()`: Fetches notes filtered by a specific category.
- `insert_note()`: Inserts a new note into the database.
- `view_note()`: Retrieves a single note by its ID. Used for endpoints like the edit and delete endpoint.
- `delete_note()`: Deletes a note from the database.
- `edit_note()`: Updates an existing note with new information.

This file also contains route definitions for:
- The homepage (`/`) that displays all notes.
- Category-based pages (`/note/<category>`) that display notes filtered by category.
- Pages to create, edit, and delete notes (`/note/new`, `/edit/<id>`, `/delete/<id>`).

### 2. **templates/**
This directory contains the HTML templates for rendering the web pages:
- **`layout.html`**: The base template that includes the common structure such as the navigation bar used across all pages.
- **`index.html`**: Displays all the notes.
- **`new_note.html`**: The form for creating a new note.
- **`edit.html`**: The form for editing an existing note.
- **`delete.html`**: A confirmation page for deleting a note.
- **Category-specific templates**: Pages to display notes filtered by categories like School, Work, Hobbies, and Other.

### 3. **static/styles.css**
This file contains custom CSS for styling the buttons of the application. It defines button styles (`btn-edit-primary`, `btn-delete-primary`). Custom button styles were created to match the rest of the custom color theme. With the exception of the custom buttons, all other css customization was done with inline css for simplicity.

### 4. **notebook.db**
This is the SQLite database file that stores all the notes. It includes a single table, `notes`, with columns for:
- `id`: The primary key (auto-incremented).
- `category`: The category of the note (e.g., School, Work).
- `title`: The title of the note.
- `content`: The content of the note.
- `date`: The date when the note was created.

## How It Works

The Digital Notebook app uses Flask to handle requests from the user and SQLite to manage data persistence. The application provides various endpoints to interact with the notes:
- **GET /**: Displays all notes.
- **GET /note/<category>**: Displays notes filtered by the specified category.
- **GET /note/new**: Displays the form for creating a new note.
- **POST /note/new**: Submits a new note to the database.
- **GET /edit/<id>**: Displays the form for editing an existing note.
- **POST /edit/<id>**: Submits the changes to the existing note.
- **GET /delete/<id>**: Displays a confirmation page to delete a note.
- **POST /delete/<id>**: Deletes the note from the database.

The application uses SQLite to persist data, with each note having its category, title, content, and date. The routes for creating, editing, and deleting notes ensure that the user's changes are reflected in the database in real time.

## Design Choices

### Categories
The decision to hard-code the categories (School, Work, Hobbies, and Other) was made to simplify the development of the application. While dynamic category management (allowing users to create custom categories) would provide more flexibility, the predefined set of categories is sufficient for this application and helps keep the user experience simple.

### Bootstrap
The decision to use Bootstrap for styling was made to save development time while ensuring a responsive and mobile-friendly layout. Bootstrap provides a variety of ready-made components like navigation bars, buttons, and form controls that streamline the development process.

### SQLite Database
SQLite was chosen as the database due to its simplicity and ease of integration with Flask. It requires minimal setup and is perfect for a small-scale application like the Digital Notebook. Although a more powerful database system like PostgreSQL or MySQL could be used for scaling, SQLite is more than sufficient for this project.
