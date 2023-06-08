-- SQL-команды для создания таблиц


create table employees_data
(
    employees_id int primary key,
	first_name varchar(100) not null,
	last_name varchar(100) not null,
	title  varchar(100),
	birth_date date,
	notes text
);


create table customers_data
(
    customer_id varchar(50) primary key,
	company_name varchar(100) not null,
	contact_name varchar(100) not null
);


create table orders_data
(
    orders_id int primary key,
	customer_id varchar(50) references customers_data(customers_id) not null,
	employee_id int references employees_data(employees_id) not null,
	order_date date,
	ship_city varchar(100)
);