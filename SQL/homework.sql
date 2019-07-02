create table department (
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

-- details of each employee
SELECT employees.emp_no,employees.last_name,employees.first_name,employees.gender,salaries.salary
FROM salaries
INNER JOIN employees on 
employees.emp_no = salaries.emp_no;

-- employees who were hired in 1986
SELECT first_name, last_name, hire_date
FROM employees
WHERE hire_date 
between '1986-01-01' and  '1986-12-31';

-- list of managers
SELECT a.dept_no, a.dept_name, b.emp_no, c.last_name, c.first_name, b.from_date, b.to_date
FROM department as a
INNER JOIN dept_manager as b 
on a.dept_no = b.dept_no
Inner jOIN employees as c 
on c.emp_no = b.emp_no ;

-- list of dept employee
SELECT a.emp_no, a.last_name, a.first_name, c.dept_name
FROM employees as a 
INNER JOIN dept_emp as b 
on a.emp_no = b.emp_no
Inner Join department as c 
on b.dept_no = c.dept_no;

