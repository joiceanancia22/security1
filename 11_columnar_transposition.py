import math

plain = input("Enter Plaintext: ").upper().replace(" ", "")
cols = int(input("Enter Number of Columns: "))

rows = math.ceil(len(plain) / cols)

while len(plain) < rows * cols:
    plain += "X"

matrix = [['' for _ in range(cols)] for _ in range(rows)]

k = 0
for j in range(cols):
    for i in range(rows):
        matrix[i][j] = plain[k]
        k += 1

print("\nEncryption Matrix:")
for row in matrix:
    print(row)

cipher = ""
for i in range(rows):
    for j in range(cols):
        cipher += matrix[i][j]

print("Ciphertext:", cipher)

dmatrix = [['' for _ in range(cols)] for _ in range(rows)]

k = 0
for i in range(rows):
    for j in range(cols):
        dmatrix[i][j] = cipher[k]
        k += 1

decrypted = ""
for j in range(cols):
    for i in range(rows):
        decrypted += dmatrix[i][j]

print("Decrypted Text:", decrypted.rstrip("X"))
