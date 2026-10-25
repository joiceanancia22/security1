from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

plaintext = input("Enter plaintext: ")
key = input("Enter 16-byte key: ").encode()

if len(key) != 16:
    print("Error: Key must be exactly 16 bytes.")
    exit()

cipher = AES.new(key, AES.MODE_ECB)

ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))

decipher = AES.new(key, AES.MODE_ECB)
decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)

print("\n----- OUTPUT -----")
print("Plaintext           :", plaintext)
print("Secret Key          :", key.decode())
print("Ciphertext (Hex)    :", ciphertext.hex())
print("Decrypted Plaintext :", decrypted.decode())
