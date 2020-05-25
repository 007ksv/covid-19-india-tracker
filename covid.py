import requests
r=requests.get('https://api.covid19india.org/data.json')
data=r.json()
data=data['statewise']

for i in data:
	active_case=i['active']
	state=i['state']
	death = i['deaths']
	recovered  = i['recovered']
	print(state)
	print('deaths= ', death)
	print('active=', active_case)
	print('recovered', recovered)
	print('*'*30)
