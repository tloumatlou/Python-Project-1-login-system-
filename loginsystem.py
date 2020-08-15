A=input("Do you have an account? Y/N: ")
def login(p):
	name=input("Enter username: ")
	while True:
		pas=input("Enter password: ")
		if pas ==p:
			print("Access granted!")
			break
		else:
			print("Access denied!")

if A=="Y":
	login("123$@")#Default password
else:
	new=input("Do you want to create a new account? Y/N ")
	if new=="N":
		print("Goodbye!")
	else:
		newname=input("Enter name: ")
		while True:
			newpas=input("Enter password: ")
			cpass=input("Confirm password:")
			if newpas != cpass:
				print("Passwords don't match!")
			else:
				print("Created account")
				break
	
