"""Скрипт для заполнения данными таблиц в БД Postgres."""

import csv
import psycopg2


def open_csv_file(path):
    """Возвращает список словарей"""
    with open(path, 'r', encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter=",")
        data = []
        for line in file_reader:
            data.append(line)

    return data


#  параметры подключения к базе данных
params = psycopg2.connect(host="localhost", database="north", user="postgres", password="777777")
try:
    with params:
        with params.cursor() as cur:

            employees = open_csv_file('../homework-1/north_data/employees_data.csv')  # открытие файла employees_data

            for i_employees in employees:  # заполнение данными таблицы employees_data
                cur.execute('INSERT INTO employees_data (employee_id, first_name, last_name, title, birth_date, notes)'
                            ' VALUES (%s, %s, %s, %s, %s, %s)',
                            (i_employees[0], i_employees[1],
                             i_employees[2], i_employees[3],
                             i_employees[4], i_employees[5]))

            customers = open_csv_file('../homework-1/north_data/customers_data.csv')  # открытие файла customers

            for i_customers in customers:  # заполнение данными таблицы customers_data
                cur.execute('insert into customers_data values (%s, %s, %s)',
                            (i_customers[0], i_customers[1], i_customers[2]))

            orders = open_csv_file('../homework-1/north_data/orders_data.csv')  # открытие файла orders_data

            for i_orders in orders:  # заполнение данными таблицы orders_data
                cur.execute('insert into orders values (%s, %s, %s, %s, %s)',
                            (i_orders[0], i_orders[1], i_orders[2],
                             i_orders[3], i_orders[4]))
finally:
    params.close()
