import sqlite3

# 创建一个数据库 没有会自动创建
conn = sqlite3.connect('test.db')

# 创建一个游标对象
cursor = conn.cursor()


def testMain():
    # 创建一个表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    # 插入数据
    cursor.execute('''
        INSERT INTO users (name, email) VALUES (?, ?)
    ''', ('John Doe', 'john@example.com'))
    # 提交更改
    conn.commit()

def search():
    cursor.execute('select * from users')
    rows =cursor.fetchall()
    for row in rows:
        print(row)

def closeConn():
    '''关闭游标'''
    cursor.close()
    '''关闭连接'''
    conn.close()

if __name__ == '__main__':
    # testMain()
    search()
    closeConn()