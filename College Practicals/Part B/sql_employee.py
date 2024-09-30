import sqlite3

conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employee 
    (
        EMPNO INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        SALARY INT NOT NULL
    );
    ''')

def insert_employee():
    empno = int(input('\nEnter employee number: '))
    name = input('Enter name: ')
    salary = int(input('Enter salary: '))
    
    try:
        cursor.execute('INSERT INTO employee(EMPNO, NAME, SALARY) VALUES (?, ?, ?)', (empno, name, salary))
        conn.commit()
        print('Record inserted successfully!')
    except Exception as e:  #sqlite3.IntegrityError alternative
        print('Record with same empno already exists!')


def display_employee():
    empno = int(input('\nEnter empno of the employee: '))
    
    cursor.execute('SELECT * FROM employee WHERE EMPNO = ?', (empno,))
    row = cursor.fetchone()
    
    if row is None:
        print('\nNo Record Found!')
    else:
        print('\nEmpno:', row[0])
        print('Name:', row[1])
        print('Salary:', row[2])

def salary_range():
    min_sal = int(input('\nEnter minimum salary: '))
    max_sal = int(input('Enter maximum salary: '))
    
    cursor.execute('SELECT * FROM employee WHERE SALARY BETWEEN ? AND ?', (min_sal, max_sal))
    rows = cursor.fetchall()
    
    if len(rows) == 0:
        print('No records within salary range.')
    else:
        for row in rows:
            print('Empno:', row[0])
            print('Name:', row[1])
            print('Salary:', row[2])
            print('--------------')

while True:
    print('\n------Menu------')
    print('1. Insert employee record')
    print('2. Display employee record')
    print('3. Display employees within salary range')
    print('4. Exit')
    
    choice = int(input('Enter your choice [1-4] : '))
    
    if choice == 1:
        insert_employee()
    elif choice == 2:
        display_employee()
    elif choice == 3:
        salary_range()
    elif choice == 4:
        print('\nExiting.....')
        break
    else:
        print('\nInvalid choice. Please try again.')

conn.close()