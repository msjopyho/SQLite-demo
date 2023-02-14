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

print(emp_1.first)
print(emp_1.last)
print(emp_1.pay)


#c.execute("INSERT INTO employees VALUES ('Mary', 'Schafer', 70000)")

#conn.commit()

c.execute("select * from employees where last = 'Schafer'")

#print(c.fetchone()) #get next row in results and only return that row
print(c.fetchall()) #get other rows as list


conn.commit() #commit first transaction

conn.close()