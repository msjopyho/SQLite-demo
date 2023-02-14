import sqlite3
from employee import Employee

# create and connect a database file
conn = sqlite3.connect(':memory:')
# using a :memory: connection allows for each run to be a clean database
# can pass it into a file when ready 'file.db'

# create cursor to execute commands
c = conn.cursor()


# Create table: only execute once! unless using ":memory:"
c.execute("""CREATE TABLE employees(
            first text,
            last text,
            pay integer
            )""") #""" = doc string without breaks

def insert_emp(emp):
    c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
              {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    c.execute("select * from employees where last =:last", {'last': lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})


emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 60000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print(emps)

# # using DB API placeholder to input
# # using tuple for all the values
# # c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
# #
# # conn.commit()
# #
# # #dictionary method
# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
#           {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
# #
# # conn.commit()
#
# c.execute("select * from employees where last = ?", ('Schafer',))
#
# # print(c.fetchone()) #get next row in results and only return that row
# print(c.fetchall())  # get other rows as list
#
# c.execute("select * from employees where last =:last", {'last': 'Doe'})
#
# print(c.fetchall())  # get other rows as list
#
# conn.commit()  # commit first transaction

conn.close()
