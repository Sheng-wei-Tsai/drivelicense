country = input('Where are you from: ')
age = input('How old are you: ')
age = int(age)
if country == 'taiwan':
	if age >= 18:
		print('you can get drivelicense')  
	else:
		print('you cannot get drivelicense')
elif country == 'american':
	if age >= 16:
		print('you can get drivelicense')
	else: 
		print('you cannot get drivelicense')

		

