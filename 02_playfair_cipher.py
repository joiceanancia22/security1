keyword = input("Enter keyword: ").upper().replace("J", "I")
plaintext = input("Enter plaintext: ").upper().replace("J", "I")

key = ""

for ch in keyword:
    if ch.isalpha() and ch not in key:
        key += ch

for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
    if ch not in key:
        key += ch

matrix = [list(key[i:i + 5]) for i in range(0, 25, 5)]

print("\nKey Matrix:")
for row in matrix:
    print(" ".join(row))

plaintext = "".join(ch for ch in plaintext if ch.isalpha())
text = ""
i = 0

while i < len(plaintext):
    a = plaintext[i]

    if i + 1 < len(plaintext):
        b = plaintext[i + 1]

        if a == b:
            text += a + "X"
            i += 1
        else:
            text += a + b
            i += 2
    else:
        text += a + "X"
        i += 1

if len(text) % 2 != 0:
    text += "X"

print("\nProcessed Plaintext:", text)

cipher = ""

for i in range(0, len(text), 2):
    a = text[i]
    b = text[i + 1]

    for r in range(5):
        for c in range(5):
            if matrix[r][c] == a:
                r1, c1 = r, c
            if matrix[r][c] == b:
                r2, c2 = r, c

    if r1 == r2:
        cipher += matrix[r1][(c1 + 1) % 5]
        cipher += matrix[r2][(c2 + 1) % 5]
    elif c1 == c2:
        cipher += matrix[(r1 + 1) % 5][c1]
        cipher += matrix[(r2 + 1) % 5][c2]
    else:
        cipher += matrix[r1][c2]
        cipher += matrix[r2][c1]

print("\nEncrypted Text:", cipher)

decrypted = ""

for i in range(0, len(cipher), 2):
    a = cipher[i]
    b = cipher[i + 1]

    for r in range(5):
        for c in range(5):
            if matrix[r][c] == a:
                r1, c1 = r, c
            if matrix[r][c] == b:
                r2, c2 = r, c

    if r1 == r2:
        decrypted += matrix[r1][(c1 - 1) % 5]
        decrypted += matrix[r2][(c2 - 1) % 5]
    elif c1 == c2:
        decrypted += matrix[(r1 - 1) % 5][c1]
        decrypted += matrix[(r2 - 1) % 5][c2]
    else:
        decrypted += matrix[r1][c2]
        decrypted += matrix[r2][c1]

print("Decrypted Text:", decrypted)
