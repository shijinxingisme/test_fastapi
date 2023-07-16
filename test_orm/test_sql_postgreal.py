import psycopg2
from psycopg2 import Error

# pip install psycopg2


connection = psycopg2.connect(
    host='localhost',
    database='mytest',
    user='postgres',
    password='root'
)
if connection:
    print('Connected to PostgreSQL database')


def create_table(query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
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
def insert_update_record(query, record_data):
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
    # query ="""
    #     CREATE TABLE users (
    #         id SERIAL PRIMARY KEY,
    #         name VARCHAR(255),
    #         email VARCHAR(255)
    #     )
    # """
    # create_table(query)

    # query = "INSERT INTO users ( name, email) VALUES ( %s, %s)"
    # record_data = ("John Doe", "johndoe@example.com")
    # insert_update_record(query,record_data)

    read_records("select * from users")

    # delete_record("delete from users where id = 1")
