import requests

ua_response = requests.get('https://russianwarship.rip/api/v2/war-info/status/ua')
ua_data = ua_response.json()
ua_data1 = ua_response.status_code
en_response = requests.get('https://russianwarship.rip/api/v2/war-info/status/en')
en_data = en_response.json()


print(f"This is data in Ukrainian: {ua_data},{ua_data1}")
print(f"This is data in English: {en_data}")

latest_response = requests.get("https://russianwarship.rip/api/v2/war-info/status/")    
latest_data = latest_response.json()

print(latest_data)


date_response = requests.get('https://russianwarship.rip/api/v2/statistics/2022-02-25')
date_data = date_response.json()
print(date_data)

date1_response = requests.get('https://russianwarship.rip/api/v2/statistics/2022-08-19')
date1_data = date1_response.json()
print(date1_data)

