errors = ["email", "password"]

error_map = {
    **{field: f"{field} is required" for field in errors},
    "data": "new data"
}

print(error_map)


for i in range(1, 6, 2):
    print(i)
for i in range(3):
    for j in range(2):
        print(i, j)
for i in range(1, 5):
    print(i)
