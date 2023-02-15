
import sqlite3
import createDB as cd

db = cd.sqlite3.connect(':memory:')  # Using an in-memory database
cur = cd.db.cursor()

# One useful aggregation function is AVG, which you can use to compute the mean of a given result set:
cur.execute('''SELECT itemid, AVG(price) FROM BoughtItem GROUP BY itemid''')
print(cur.fetchall())


# make the above output easier to underestand
cur.execute('''SELECT item.title, AVG(boughtitem.price) FROM BoughtItem as boughtitem INNER JOIN Item as item on (item.id = boughtitem.itemid) GROUP BY boughtitem.itemid''')
print(cur.fetchall())