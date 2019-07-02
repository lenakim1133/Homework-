-- 1. details of each employee
SELECT employees.emp_no,employees.last_name,employees.first_name,employees.gender,salaries.salary
FROM salaries
INNER JOIN employees on 
employees.emp_no = salaries.emp_no;

-- 2. employees who were hired in 1986
SELECT first_name, last_name, hire_date
FROM employees
WHERE hire_date 
between '1986-01-01' and  '1986-12-31';

-- 3. list of managers
SELECT a.dept_no, a.dept_name, b.emp_no, c.last_name, c.first_name, b.from_date, b.to_date
FROM department as a
INNER JOIN dept_manager as b 
on a.dept_no = b.dept_no
Inner jOIN employees as c 
on c.emp_no = b.emp_no ;

-- 4. list of dept employee
SELECT a.emp_no, a.last_name, a.first_name, c.dept_name
FROM employees as a 
INNER JOIN dept_emp as b 
on a.emp_no = b.emp_no
Inner Join department as c 
on b.dept_no = c.dept_no;

-- 5. employee named "hercules" with last names with "b"
SELECT first_name, last_name 
FROM employees
WHERE first_name like 'Hercules' and  last_name like 'B%'


-- 6. list of sales dept 
SELECT b.emp_no, b.last_name, b.first_name, a.dept_name
FROM dept_emp as c 
INNER JOIN employees as b
ON c.emp_no = b.emp_no
INNER JOIN department as a 
ON a.dept_no = c.dept_no
WHERE a.dept_name like 'Sales'

-- 7. list of employees in sales and development dept
SELECT b.emp_no, b.last_name, b.first_name, a.dept_name
FROM dept_emp as c 
INNER JOIN employees as b
ON c.emp_no = b.emp_no
INNER JOIN department as a 
ON a.dept_no = c.dept_no
WHERE a.dept_name like 'Sales' or a.dept_name like 'Development'

-- 8. list of the frequency count of employee last names
SELECT last_name, COUNT(last_name) as last_name_count
FROM employees
GROUP BY last_name
Order by last_name_count DESC;
