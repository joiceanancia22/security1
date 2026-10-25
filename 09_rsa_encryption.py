from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)
public_key = key.publickey()

text = input("Enter Plaintext: ")

cipher = PKCS1_OAEP.new(public_key)
encrypted = cipher.encrypt(text.encode())

cipher = PKCS1_OAEP.new(key)
decrypted = cipher.decrypt(encrypted).decode()

print("Ciphertext:", encrypted.hex())
print("Decrypted Text:", decrypted)
