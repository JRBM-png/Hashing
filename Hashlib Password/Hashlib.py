import hashlib

h = hashlib.sha256() #This is a hashing algorithm, it takes an input and produces a fixed-size string of bytes
correct_password = "password123"
h.update(correct_password.encode())

password_hash = h.hexdigest() #This would be stored in a database
print(password_hash)

user_input = "password123" #To test this change the password, run the program and compare the hash
h=hashlib.new("sha256")
h.update(user_input.encode())
input_hash = (h.hexdigest())

#Stops you from storing it in clear text, you would hash the user input and compare it to the stored hash. If they match, the password is correct.

#Added security by not storing the password in clear text, even if the database is compromised, the attacker would only have access to the hash, not the actual password.

print(input_hash) == password_hash