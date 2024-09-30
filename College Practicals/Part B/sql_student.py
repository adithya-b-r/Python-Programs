import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS student
    (
        REGNO INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        SUB1_MARKS INT NOT NULL,
        SUB2_MARKS INT NOT NULL,
        SUB3_MARKS INT NOT NULL
    );
    ''')

def insert_student():
    regno = int(input("Enter regno : "))
    name = input("Enter name : ")
    sub1 = int(input("Enter marks in subject 1: "))
    sub2 = int(input("Enter marks in subject 2: "))
    sub3 = int(input("Enter marks in subject 3: "))

    try:
        cursor.execute('INSERT INTO student (REGNO, NAME, SUB1_MARKS, SUB2_MARKS, SUB3_MARKS) VALUES (?,?,?,?,?)',
                       (regno, name, sub1, sub2, sub3)) #type in same line.
        conn.commit()
        print('Record inserted successfully!')
    except Exception as e:  #sqlite3.IntegrityError alternative
        print('Record with same regno already exists!')

def display_student():
    cursor.execute('SELECT * FROM student')
    rows = cursor.fetchall()

    if len(rows) == 0:
        print('\nNo Record Found!')
    else:
        for row in rows:
            print('REGNO : ', row[0])
            print('NAME : ', row[1])
            print('Sub 1 : ', row[2])
            print('Sub 2 : ', row[3])
            print('Sub 3 : ', row[4])
            print('------------------')

def delete_student():
    regno = int(input("Enter regno of student to delete : "))
    cursor.execute('SELECT * FROM student WHERE REGNO=?', (regno,))
    row = cursor.fetchone()
    if row is None:
        print('No record found.')
    else:
        cursor.execute('DELETE FROM student WHERE REGNO=?', (regno,))
        conn.commit()
        print('Record deleted successfully!')

while True:
    print('\n---------MENU---------')
    print('1. Insert student record')
    print('2. Display records')
    print('3. Delete record')
    print('4. Exit')
    choice = int(input("Enter your choice [1-4] : "))
    if choice == 1:
        insert_student()
    elif choice == 2:
        display_student()
    elif choice == 3:
        delete_student()
    elif choice == 4:
        print('\nExiting...')
        break
    else:
        print('\nInvalid choice! try again...')

conn.close()