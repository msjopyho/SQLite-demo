import sqlite3

#create and connect a database file
conn = sqlite3.connect('employee.db')

#create cursor to execute commands
c = conn.cursor()

# Create table: only execute once!
# c.execute("""CREATE TABLE employees(
#             first text,
#             last text,
#             pay integer
#             )""") #""" = doc string without breaks

c.execute("INSERT INTO employees VALUES ('Corey', 'Schafer', 50000)")

conn.commit() #commit first transaction

conn.close()