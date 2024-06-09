'''
Practical Task 1 SQLite
'''

# importing
import sqlite3

# creating the database
db = sqlite3.connect("python_programing_db.db")

cursor = db.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS python_program(
               id INTEGER PRIMARY KEY, 
               name TEXT, 
               grade INTEGER)
               ''')

db.commit()

# inserting data
id10 = 55
name10 = "Carl Davis"
grade10 = 61

id11 = 66
name11 = "Dennis Fredrickson"
grade11 = 88

id12 = 77
name12 = "Jane Richards"
grade12 = 78

id13 = 12
name13 = "Peyton Sawyer"
grade13 = 45

id14 = 2
name14 = "Lucas Brooke"
grade14 = 99

students_grades = [(id10, name10, grade10), (id11, name11, grade11), (id12, name12, grade12), (id13, name13, grade13), (id14, name14, grade14)]

cursor.executemany(''' INSERT INTO python_program(id, name, grade) VALUES(?,?,?)''', students_grades)

db.commit()

# retrieving all data with a grade between 60 and 80
grade1 = 60
grade2 = 80

cursor.execute('''SELECT name, grade FROM python_program WHERE grade >= ? AND grade <= ?''', (grade1, grade2))

for row in cursor:
    # row[0] returns the first column in the query (name), row[1] returns the grade column
    print('{0} : {1}'.format(row[0], row[1]))

# changing Carl Davis's grade to 65
grade3 = 65
id1 = 55

cursor.execute('''UPDATE python_program SET grade = ? WHERE id = ? ''', (grade3, id1))

db.commit()

# deleting Dennis Fredrickson's row
id2 = 66

cursor.execute('''DELETE FROM python_program WHERE id = ? ''', (id2,))

db.commit()

# change the grade of all students with an id greater than 55 to a grade of 80.
id3 = 55
grade2 = 80

cursor.execute('''UPDATE python_program SET grade = ? WHERE id > ? ''', (grade2, id3))

db.commit()

# closing the database connection
db.close()
