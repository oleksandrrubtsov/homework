list1 = list(range(1,101))

result_list = []
i = 0 
while i < len(list1):
    num = list1[i]
    if num % 7 == 0 and num % 5 != 0:
        result_list.append(num)
    i += 1

print(result_list)  
