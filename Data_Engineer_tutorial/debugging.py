
import sqlite3
import createDB as cd

db = cd.sqlite3.connect(':memory:')  # Using an in-memory database
cur = cd.db.cursor()


cur.execute('''EXPLAIN QUERY PLAN SELECT customer.firstname, item.title, item.price, boughtitem.price FROM BoughtItem as boughtitem INNER JOIN Customer as customer on (customer.id = boughtitem.customerid) INNER JOIN Item as item on (item.id = boughtitem.itemid)''')

print(cur.fetchall())