
import sqlite3
import createDB as cd

db = cd.sqlite3.connect(':memory:')  # Using an in-memory database
cur = cd.db.cursor()

cur.execute('''SELECT customer.firstname, SUM(boughtitem.price) FROM BoughtItem as boughtitem INNER JOIN Customer as customer on (customer.id = boughtitem.customerid) GROUP BY customer.firstname''')

print(cur.fetchall())
