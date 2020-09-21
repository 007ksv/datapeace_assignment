import request

url = 'http://localhost:8000/api/users/'

def menu():
	print('''
		1. fetch user
		2. Create new user
		3. Update User detail
		4. Special search query
		''')
def main():
	c = input("Enter > ")

	if c == '1':
		resp = request.get(url)
		if resp.status_code == 200:
			print(resp.json())
		else:
			print("some error\n")
	elif c == '2':
		print("Enter Users Detail")
		first_name = input("Enter first name > ")
		last_name = input("Enter Last name > ")
		email = input("Enter email > ")
		company_name = input("Enter company_name > ")
		city = input("Enter city > ")
		state = input("Enter state > ")
		age = int(input("Enter age > "))
		zip = int(input("Enter zip > "))
		web = input("Enter web > ")
		data = {
			'first_name': first_name,
			'last_name': last_name,
			'email': email,
			'country_name': country_name
		}

