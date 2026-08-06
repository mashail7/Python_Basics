name = str(input())
password = str(input())

password_try = str(input())

while password_try != password:
    password_try = str(input())

print(f"Welcome {name}!")