import sqlite3

# conn = sqlite3.connect('/home/control/PycharmProjects/PiPos/db/posSys.db')
conn = sqlite3.connect('/home/control/PycharmProjects/PiPos/db/new.db')
# conn = sqlite3.connect('/home/control/PycharmProjects/Aphoras/pos.db') # trial


def retrieve_password(uname):
    global conn
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE name = ?", (uname,))
    return str(cursor.fetchone()[0])  # convert the unicode string to regular string


def create_user(name, pwd):
    global conn
    conn.execute("INSERT INTO users (name, password) VALUES (?,?)", (name, pwd))
    conn.commit()


def get_users():
    global conn
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM users")
    return sorted([str(i[0]) for i in cursor.fetchall()])


def delete_user(uname):
    global conn
    conn.execute("DELETE FROM users WHERE name = ?", (uname,))
    conn.commit()


def search(item):
    item_name = item + '%'
    global conn
    cursor = conn.cursor()
    cursor.execute("SELECT name, description, price FROM items WHERE name LIKE ?", (item_name,))
    # returns a list of tuples
    a = cursor.fetchall()
    z = []
    for i in range(len(a)):
        x = []
        for j in range(3):
            t = a[i][j]
            x.append(str(t).rstrip())
        z.append(x)
    return z


def search_inventory(item):
    item_name = item + '%'
    global conn
    cursor = conn.cursor()
    cursor.execute("SELECT ID, name, description, stock, price, barcode FROM items WHERE name LIKE ?", (item_name,))
    # returns a list of tuples
    a = cursor.fetchall()
    z = []
    for i in range(len(a)):
        x = []
        for j in range(5):
            t = a[i][j]
            x.append(str(t).rstrip())
        z.append(x)
    return z


def delete_item(item_id):
    global conn
    conn.execute("DELETE FROM items WHERE ID = ?", (item_id,))
    conn.commit()


def get_item_details(item_id):
    global conn
    cursor = conn.cursor()
    cursor.execute("SELECT ID, name, description FROM items WHERE ID = ?", (item_id,))
    a = cursor.fetchall()[0]
    z = []
    for i in range(3):
        z.append(str(a[i]).rstrip())
    return z


def update(item_id, name, desc):
    global conn
    conn.execute("UPDATE items set name = ?, description=? where ID=?", (name, desc, item_id))
    conn.commit()


def add_new_item(name, quantity, price, description, barcode):
    global conn
    conn.execute("INSERT INTO items (name, description, barcode, stock, price) VALUES (?, ?, ?, ?, ?)",
                 (name, description, barcode, quantity, price))
    conn.commit()


def make_sale(total_amount):
    conn.execute("INSERT INTO sales (total) VALUES (?)", (total_amount))

