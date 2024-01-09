--1.write a query in SQL to display the first name, last name, department number, and department name for each employee
--2.write a query in SQL to display the first and last name, department, city, and state province for each employee
--3.write a query in SQL to display the first name, last name, department number, and department name, for all employees for departments 80 or 40
--4.write a query in SQL to display all departments including those where does not have any employee
--5.write a query in SQL to display the first name of all employees including the first name of their manager
--6.write a query in SQL to display the job title, full name (first and last name ) of the employee, and the difference between the maximum salary for the job and the salary of the employee
--7.write a query in SQL to display the job title and the average salary of employees
--8.write a query in SQL to display the full name (first and last name), and salary of those employees who work in any department located in London
--9.write a query in SQL to display the department name and the number of employees in each department


--1
select e.first_name, e.last_name, d.department_id, d.department_name
from _employees as e 
join _department as d on e.department_id = d.department_id

--2
select e.first_name, e.last_name, d.depart_name, l.city, l.state_province
from _employees as e
join _departments as d on e.department_id = d.department_id
join _locations as l on d.location_id = l.location_id

--3
select e.first_name, e.last_name, d.department_id, d.department_name
from _employees e 
join _department d on e.department_id = d.department_id
where d.department_id in  (80,40) 

--4
select  department_id, department_name
from _department d
ORDER BY department_id;

--5
select 
  e.first_name AS employee_first_name,
  m.first_name AS manager_first_name
from _employees e
left join _employees m on e.manager_id = m.employee_id; 

--6
select e.first_name, e.salary, j.job_title, j.max_salary
from _employees e
join _jobs j on e.job_id = j.job_id
order by j.max_salary


--7 
select job_id, avg(min_sal) as avearge_salary 
from _company_view cv 
group by job_id

--8
select concat(e.first_name, ' ', e.last_name) as full_name, e.salary
FROM _employees e
inner
 
join _departments d on e.department_id = d.department_id
inner
 
join _locations l on d.location_id = l.location_id
where l.city = 'London'

--9
select d.depart_name, count(e.employee_id) as number_of_employees
from _departments d
left
 
join _employees e on d.department_id = e.department_id
group by  d.depart_name
order by  number_of_employees desc 




