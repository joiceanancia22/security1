import numpy as np

# Hardcoded 2x2 key matrix
key = np.array([[3, 3],
                [2, 5]])

plain = input("Enter Plaintext: ").upper().replace(" ", "")

if len(plain) % 2 != 0:
    plain += "X"

nums = []
for ch in plain:
    nums.append(ord(ch) - 65)

p = np.array(nums).reshape(-1, 2).T

print("Plaintext Matrix:")
print(p)

cipher_matrix = np.dot(key, p) % 26

print("Encrypted Matrix:")
print(cipher_matrix)

cipher = ""
rows = len(cipher_matrix)
cols = len(cipher_matrix[0])

for j in range(cols):
    for i in range(rows):
        cipher += chr(cipher_matrix[i][j] + 65)

print("Ciphertext:", cipher)

det = key[0][0] * key[1][1] - key[0][1] * key[1][0]
det = det % 26

det_inv = None
for i in range(26):
    if (det * i) % 26 == 1:
        det_inv = i
        break

if det_inv is None:
    print("Key matrix has no modular inverse. Decryption is not possible.")
    exit()

adj = np.array([[key[1][1], -key[0][1]],
                [-key[1][0], key[0][0]]])

inv_key = (det_inv * adj) % 26

print("Inverse Key Matrix:")
print(inv_key)

plain_matrix = np.dot(inv_key, cipher_matrix) % 26

print("Decrypted Matrix:")
print(plain_matrix)

decrypted = ""
rows = len(plain_matrix)
cols = len(plain_matrix[0])

for j in range(cols):
    for i in range(rows):
        decrypted += chr(plain_matrix[i][j] + 65)

print("Decrypted Text:", decrypted)
