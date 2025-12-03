from werkzeug.security import generate_password_hash

password = "password"
hashed_password = generate_password_hash(password)
print(hashed_password)