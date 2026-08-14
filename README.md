A desktop scheduling application with a MySQL backend, built as the final project for FIU's Database Systems course (Group 6, COP4710, Spring 2026). The app provides a customtkinter GUI for managing schedules, backed by a normalized relational schema with full CRUD operations, constraints, and sample data.

Files: Schema.sql (full relational schema, tables, keys, constraints), data.sql (sample data for local setup), queries.sql and constraints_test.sql (query and constraint validation examples), SQLHandler.py (database access layer), UIHandler.py and main.py (GUI application logic).

IMPORTANT: In the SQLHandler.py file, update the database variables to include YOUR database hostname, username, password, and database name. Otherwise, the program will have no way of interacting with your database.

To run this, you will need to install a few Python libraries which do not come installed by default: mysql-connector-python, customtkinter, tkcalendar.

When running from an IDE, you should run from the UIHandler.py file. Ensure you already have created a MySQL database with the proper tables and constraints. You can use the Schema.sql file along with the sample data in it to set it up easily.
