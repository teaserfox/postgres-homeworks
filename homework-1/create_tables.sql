-- SQL-команды для создания таблиц


CREATE TABLE employees
(
    employee_id int PRIMARY KEY,
	first_name varchar(100) not null,
	last_name varchar(100) not null,
	title  varchar(100),
	birth_date date,
	notes text
);


CREATE TABLE customers
(
    customer_id varchar(50),
	company_name varchar(100) not null,
	contact_name varchar(100) not null
);


CREATE TABLE orders
(
    orders_id int primary,
	customer_id varchar(50) references customers(customer_id) not null,
	employee_id int references employees(employee_id) not null,
	order_date date,
	ship_city varchar(100)
);