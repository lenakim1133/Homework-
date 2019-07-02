CREATE TABLE department (
dept_no VARCHAR NOT NULL,
dept_name VARCHAR 
);


Create TABLE dept_emp (
emp_no INTEGER,
dept_no VARCHAR NOT NULL,
from_date DATE,
to_date DATE
);

CREATE TABLE dept_manager(
dept_no VARCHAR NOT NULL,
emp_no INTEGER,
from_date DATE,
to_date DATE
);


CREATE TABLE employees (
emp_no INTEGER,
birth_date DATE,
first_name VARCHAR,
last_name VARCHAR,
gender VARCHAR,
hire_date DATE
);

CREATE TABLE salaries (
emp_no INTEGER,
salary INTEGER,
from_date DATE,
to_date DATE
);

CREATE TABLE titles (
emp_no INTEGER,
title VARCHAR,
from_date DATE,
to_date DATE
);