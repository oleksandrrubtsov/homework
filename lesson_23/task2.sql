SELECT first_name AS "First Name", last_name AS "Last Name"
FROM "_employees" e ;

select department_id 
from "_employees" e ;

SELECT * FROM "_employees" e
ORDER BY first_name DESC;

select first_name, last_name, salary, salary * 0.12 AS PF 
from "_employees" e ;

select max(salary), min(salary) 
from "_employees" e 

select first_name, last_name, round(salary / 12.0, 2) as monthly_salary
from "_employees" e 