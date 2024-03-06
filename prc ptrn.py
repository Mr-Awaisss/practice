rows = int(input("Enter the number of rows: "))

# Print the first triangle
for i in range(rows):
    for j in range(i, rows):
        print("*", end='')
    print(end=' ')

# Print space between the triangles
print(end=' ')

# Print the second triangle
for i in range(rows):
    for j in range(i, rows):
        print("*", end='')
    print()
    for k in range(0, i + 1):
        print(" ", end='')
