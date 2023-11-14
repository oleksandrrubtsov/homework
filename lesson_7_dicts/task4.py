days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

dict = {i: day for i, day in enumerate(days_of_week,1)}
print(dict) 

my_dict1 = {day: i + 1 for i, day in enumerate(days_of_week)}
print(my_dict1)