import mysql.connector
from mysql.connector import Error


def init():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='your_database',
            user='your_username',
            password='your_password'
        )
        if connection.is_connected():
            print('Connected to MySQL database')
    except Error as e:
        print(f'Error connecting to MySQL database: {e}')


# Create a new record
def create_record(connection, query, record_data):
    try:
        cursor = connection.cursor()
        cursor.execute(query, record_data)
        connection.commit()
        print('Record created successfully')
    except Error as e:
        print(f'Error creating record: {e}')


# Read records
def read_records(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        for record in records:
            print(record)
    except Error as e:
        print(f'Error reading records: {e}')


# Update a record
def update_record(connection, query, record_data):
    try:
        cursor = connection.cursor()
        cursor.execute(query, record_data)
        connection.commit()
        print('Record updated successfully')
    except Error as e:
        print(f'Error updating record: {e}')


# Delete a record
def delete_record(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print('Record deleted successfully')
    except Error as e:
        print(f'Error deleting record: {e}')


if __name__ == '__main__':
    init()
