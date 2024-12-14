import pymysql


def connect_to_mysql():
    # Connect to MySQL database
    db = pymysql.connect(host='localhost', port=3306, user='root', password='acui192006', charset='utf8')
    cursor = db.cursor()

    cursor.execute('select version()')  # Check MySQL version
    data = cursor.fetchall()
    print('mysql version:{}'.format(data))

    db.close()  # Close database connection


def create_new_mysql():
    # Create new MySQL database
    db = pymysql.connect(host='localhost', port=3306, user='root', password='acui192006', charset='utf8')
    cursor = db.cursor()

    cursor.execute('create database if not exists test')  # Create new database
    print('Database created successfully.')
    db.close()  # Close database connection


def create_table():
    # Create new table in MySQL database
    db = pymysql.connect(host='localhost', port=3306, user='root', password='acui192006', db='test', charset='utf8')
    cursor = db.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age int,
    sex char(1),
    class int
)
''')
    print('Table created successfully.')
    db.close()  # Close database connection


def insert_data():
    # Insert data into MySQL table
    db = pymysql.connect(host='localhost', port=3306, user='root', password='acui192006', db='test', charset='utf8')
    cursor = db.cursor()

    cursor.execute("INSERT INTO users (name, age, sex, class) VALUES ('John', 25, 'M', 10)")
    cursor.execute("INSERT INTO users (name, age, sex, class) VALUES ('Mary', 30, 'F', 9)")
    cursor.execute("INSERT INTO users (name, age, sex, class) VALUES ('Tom', 20, 'M', 11)")
    cursor.execute("INSERT INTO users (name, age, sex, class) VALUES ('Jane', 28, 'F', 12)")

    db.commit()  # Commit changes to database
    print('Data inserted successfully.')
    db.close()  # Close database connection


def search_data():
    # Search data from MySQL table
    db = pymysql.connect(host='localhost', port=3306, user='root', password='acui192006', db='test', charset='utf8')
    cursor = db.cursor()

    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    print('Data found:')
    for row in data:
        print(row)

    db.close()  # Close database connection


def data_update():
    # Update data in MySQL table
    db = pymysql.connect(host='localhost', port=3306, user='root', password='acui192006', db='test', charset='utf8')
    cursor = db.cursor()

    cursor.execute("UPDATE users SET age = 18 WHERE name = 'John'")
    db.commit()  # Commit changes to database
    print('Data updated successfully.')
    db.close()  # Close database connection


def data_delete():
    # Delete data from MySQL table
    db = pymysql.connect(host='localhost', port=3306, user='root', password='acui192006', db='test', charset='utf8')
    cursor = db.cursor()

    cursor.execute("DELETE FROM users WHERE age = 20")
    db.commit()  # Commit changes to database
    print('Data deleted successfully.')
    db.close()  # Close database connection


if __name__ == '__main__':
    # connect_to_mysql()
    # create_new_mysql()
    # create_table()
    # insert_data()
    # search_data()
    # data_update()
    data_delete()
