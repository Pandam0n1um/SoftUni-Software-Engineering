username = str(input())
password = str(input())
data = str(input())

while not (data == password):
    data = str(input())

print(f"Welcome {username}!")
