import pymysql.cursors
from datetime import datetime

# Connect to MySQL database
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='123',
                       database='InternDetails',
                       cursorclass=pymysql.cursors.DictCursor)

print("Connection to MySQL database established successfully!")

try:
    conn.ping()
    print("Connected to MySQL database successfully!")
except pymysql.Error as e:
    print("Error:", e)


# Create table if not exists
with conn.cursor() as cursor:
    cursor.execute('''CREATE TABLE IF NOT EXISTS interns (
                    intern_id INT AUTO_INCREMENT PRIMARY KEY,
                    intern_name VARCHAR(100),
                    intern_doj DATE,
                    intern_signum VARCHAR(20),
                    intern_entry_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                 )''')

    conn.commit()

# Function to create a new intern record
def create_intern(intern_name, intern_doj, intern_signum):
    try:
        with conn.cursor() as cursor:
            sql = '''INSERT INTO interns (intern_name, intern_doj, intern_signum)
                     VALUES (%s, %s, %s)'''
            cursor.execute(sql, (intern_name, intern_doj, intern_signum))
            conn.commit()
            print("Intern created successfully!")
    except pymysql.Error as e:
        print("Error:", e)
        conn.rollback()

# Function to read all intern records
def read_interns():
    try:
        with conn.cursor() as cursor:
            sql = '''SELECT * FROM interns'''
            cursor.execute(sql)
            interns = cursor.fetchall()
            return interns
    except pymysql.Error as e:
        print("Error:", e)
        conn.rollback()

# Function to read a specific intern record by ID
def read_intern(intern_id):
    try:
        with conn.cursor() as cursor:
            sql = '''SELECT * FROM interns WHERE intern_id = %s'''
            cursor.execute(sql, (intern_id,))
            intern = cursor.fetchone()
            return intern
    except pymysql.Error as e:
        print("Error:", e)
        conn.rollback()

# Function to update an existing intern record
def update_intern(intern_id, intern_name, intern_doj, intern_signum):
    try:
        with conn.cursor() as cursor:
            sql = '''UPDATE interns SET intern_name = %s, intern_doj = %s, intern_signum = %s
                     WHERE intern_id = %s'''
            cursor.execute(sql, (intern_name, intern_doj, intern_signum, intern_id))
            conn.commit()
            print("Intern updated successfully!")
    except pymysql.Error as e:
        print("Error:", e)
        conn.rollback()

# Function to delete an existing intern record
def delete_intern(intern_id):
    try:
        with conn.cursor() as cursor:
            sql = '''DELETE FROM interns WHERE intern_id = %s'''
            cursor.execute(sql, (intern_id,))
            conn.commit()
            print("Intern deleted successfully!")
    except pymysql.Error as e:
        print("Error:", e)
        conn.rollback()

# Close connection when done
def close_connection():
    conn.close()
