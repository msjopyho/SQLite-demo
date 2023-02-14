import sqlite3
from employee import Employee

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

emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 60000)

#using DB API placeholder to input
#using tuple for all the values
# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
#
# conn.commit()
#
# #dictionary method
# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
#
# conn.commit()

c.execute("select * from employees where last = ?", ('Schafer',))

#print(c.fetchone()) #get next row in results and only return that row
print(c.fetchall()) #get other rows as list

c.execute("select * from employees where last =:last", {'last': 'Doe'})

print(c.fetchall()) #get other rows as list

conn.commit() #commit first transaction

conn.close()