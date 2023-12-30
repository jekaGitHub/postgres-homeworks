"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='202312')
try:
    with conn:
        with conn.cursor() as cur:
            with open("north_data/employees_data.csv", 'r', newline='') as f:
                employees = csv.reader(f)
                next(employees)
                for employee in employees:
                    cur.execute(
                        "INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes) VALUES (%s, %s, %s, %s, %s, %s)", employee)
                cur.execute("SELECT * FROM employees")
                rows = cur.fetchall()

    with conn:
        with conn.cursor() as cur:
            with open("north_data/customers_data.csv", 'r', newline='') as f:
                customers = csv.reader(f)
                next(customers)
                for customer in customers:
                    cur.execute(
                        "INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s)", customer)
                cur.execute("SELECT * FROM customers")
                rows = cur.fetchall()

    with conn:
        with conn.cursor() as cur:
            with open("north_data/orders_data.csv", 'r', newline='') as f:
                orders = csv.reader(f)
                next(orders)
                for order in orders:
                    cur.execute(
                        "INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) VALUES (%s, %s, %s, %s, %s)", order)
                cur.execute("SELECT * FROM orders")
                rows = cur.fetchall()
finally:
    conn.close()
