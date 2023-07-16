import mysql.connector
from mysql.connector import Error

# pip install mysql-connector-python


connection = mysql.connector.connect(
    host='localhost',
    database='mydata',
    user='root',
    password='root'
)
if connection.is_connected():
    print('Connected to MySQL database')


# Create a new record
def create_record(query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print('Record created successfully')
    except Error as e:
        print(f'Error creating record: {e}')


def insert_record(query, data):
    try:
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()
        print('Record created successfully')
    except Error as e:
        print(f'Error creating record: {e}')


# Read records
def read_records(query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        for record in records:
            print(record)
    except Error as e:
        print(f'Error reading records: {e}')


# Update a record
def update_record(query, record_data):
    try:
        cursor = connection.cursor()
        cursor.execute(query, record_data)
        connection.commit()
        print('Record updated successfully')
    except Error as e:
        print(f'Error updating record: {e}')


# Delete a record
def delete_record(query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print('Record deleted successfully')
    except Error as e:
        print(f'Error deleting record: {e}')


if __name__ == '__main__':

# query = """
# CREATE TABLE IF NOT EXISTS users (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     name VARCHAR(255) NOT NULL,
#     email VARCHAR(255) NOT NULL
# )
# """
# create_record(query)

# query = "INSERT INTO users ( name, email) VALUES ( %s, %s)"
# record_data = ("John Doe", "johndoe@example.com")
# update_record(query,record_data)

# read_records("select * from users")

# delete_record("delete from users where id = 1")
