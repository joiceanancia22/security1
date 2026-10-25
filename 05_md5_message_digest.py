import hashlib

while True:
    print("\n===== MD5 MESSAGE DIGEST =====")
    print("1. Generate MD5 Message Digest")
    print("2. Verify Message Integrity")
    print("3. Demonstrate the Avalanche Effect")
    print("4. Generate MD5 Checksum for a Text File")
    print("5. Compare MD5, SHA-1 and SHA-256")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        text = input("Enter text: ")
        digest = hashlib.md5(text.encode()).hexdigest()
        print("\nMD5 Digest:", digest)

    elif choice == "2":
        text = input("Enter text: ")
        old_digest = input("Enter previous MD5 digest: ").strip()
        new_digest = hashlib.md5(text.encode()).hexdigest()

        if new_digest == old_digest:
            print("Matches - Message is not modified")
        else:
            print("Does Not Match - Message has been modified")

    elif choice == "3":
        text1 = input("Enter first string: ")
        text2 = input("Enter second string: ")

        digest1 = hashlib.md5(text1.encode()).hexdigest()
        digest2 = hashlib.md5(text2.encode()).hexdigest()

        print("\nString 1:", text1)
        print("MD5:", digest1)
        print("\nString 2:", text2)
        print("MD5:", digest2)

        if digest1 != digest2:
            print("\nAvalanche Effect: Hash values are different.")
        else:
            print("\nHash values are identical.")

    elif choice == "4":
        filename = input("Enter file path: ")

        try:
            with open(filename, "rb") as file:
                data = file.read()

            digest = hashlib.md5(data).hexdigest()
            print("\nMD5 Checksum:", digest)

        except FileNotFoundError:
            print("File not found!")

    elif choice == "5":
        text = input("Enter text: ")

        md5 = hashlib.md5(text.encode()).hexdigest()
        sha1 = hashlib.sha1(text.encode()).hexdigest()
        sha256 = hashlib.sha256(text.encode()).hexdigest()

        print("\nMD5:", md5)
        print("Length:", len(md5), "characters")
        print("\nSHA-1:", sha1)
        print("Length:", len(sha1), "characters")
        print("\nSHA-256:", sha256)
        print("Length:", len(sha256), "characters")

    elif choice == "6":
        print("Program terminated.")
        break

    else:
        print("Invalid choice! Please try again.")
