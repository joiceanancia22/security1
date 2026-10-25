from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64

key = RSA.generate(2048)
private_key = key
public_key = key.publickey()
signature = None
original_message = None

while True:
    print("\n===== DIGITAL SIGNATURE SYSTEM =====")
    print("1. Generate RSA Keys")
    print("2. Sign a Message")
    print("3. Verify Signature")
    print("4. Demonstrate Message Tampering")
    print("5. Secure Email Simulation")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        key = RSA.generate(2048)
        private_key = key
        public_key = key.publickey()
        signature = None
        original_message = None
        print("\nRSA Keys Generated Successfully!")

    elif choice == "2":
        original_message = input("Enter message to sign: ")
        hash_value = SHA256.new(original_message.encode())
        signature = pkcs1_15.new(private_key).sign(hash_value)

        print("\nSHA-256 Hash:", hash_value.hexdigest())
        print("Digital Signature:", base64.b64encode(signature).decode())
        print("Message Signed Successfully!")

    elif choice == "3":
        if signature is None:
            print("Sign a message first!")
        else:
            message = input("Enter received message: ")
            hash_value = SHA256.new(message.encode())

            try:
                pkcs1_15.new(public_key).verify(hash_value, signature)
                print("Signature Verification Successful!")
                print("Message is authentic and unchanged.")
            except (ValueError, TypeError):
                print("Signature Verification Failed!")
                print("Message may have been modified.")

    elif choice == "4":
        if signature is None:
            print("Sign a message first!")
        else:
            modified_message = original_message + " hacked"
            print("\nOriginal Message:", original_message)
            print("Tampered Message:", modified_message)

            try:
                pkcs1_15.new(public_key).verify(
                    SHA256.new(modified_message.encode()), signature
                )
                print("Verification Successful!")
            except (ValueError, TypeError):
                print("Verification Failed!")
                print("Message has been changed after signing.")

    elif choice == "5":
        message = input("Enter Alice's message: ")

        signature_email = pkcs1_15.new(private_key).sign(
            SHA256.new(message.encode())
        )

        print("\nAlice sends:", message)
        print("Message sent to Bob.")

        try:
            pkcs1_15.new(public_key).verify(
                SHA256.new(message.encode()), signature_email
            )
            print("Bob: VALID SIGNATURE")
            print("Message integrity verified.")
        except (ValueError, TypeError):
            print("Bob: INVALID SIGNATURE")

        modified = message + " hacked"
        print("\nTampered Message:", modified)

        try:
            pkcs1_15.new(public_key).verify(
                SHA256.new(modified.encode()), signature_email
            )
            print("VALID SIGNATURE")
        except (ValueError, TypeError):
            print("INVALID SIGNATURE")
            print("Message integrity failed.")

    elif choice == "6":
        print("Exiting Digital Signature System...")
        break

    else:
        print("Invalid choice! Enter a valid option.")
