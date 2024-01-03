
insert into homeworks (homework_id, subject, description, deadline, is_completed)  
values 
(1, 'Science', 'Experiment analysis', '2024-01-20', 'true'),
(2, 'English', 'Write a short essay', '2024-01-15', 'true'),

select * from homeworks 

update homeworks 
set 
	is_completed = 'false'
where homework_id = 2

insert  into homeworks (homework_id, subject, description, deadline, is_completed)  
values
(3, 'Math', 'Algebra exercises', '2024-01-15', 'true'),
(4, 'English', 'Read a novel', '2024-01-30', 'false'),
(5, 'Physics', 'E=mc^2', '2024-02-05','false')

delete from homeworks 
where subject = 'Physics'

insert into homeworks (homework_id, subject, description, deadline, is_completed)  
values
(5, 'Physics', 'E=mc^2', '2024-03-05', 'false')

update  homeworks 
set 
	is_completed = 'true'
where homework_id = 5