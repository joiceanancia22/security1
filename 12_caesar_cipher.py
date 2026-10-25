while True:
    print("\n===== Caesar Cipher Menu =====")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Brute Force Attack")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        text = input("Enter a string: ")
        shift = int(input("Enter shift value: ")) % 26

        encrypted = ""

        for ch in text:
            if ch.isupper():
                encrypted += chr((ord(ch) - 65 + shift) % 26 + 65)
            elif ch.islower():
                encrypted += chr((ord(ch) - 97 + shift) % 26 + 97)
            else:
                encrypted += ch

        print("Encrypted Cipher:", encrypted)

    elif choice == 2:
        text = input("Enter encrypted string: ")
        shift = int(input("Enter shift value: ")) % 26

        decrypted = ""

        for ch in text:
            if ch.isupper():
                decrypted += chr((ord(ch) - 65 - shift) % 26 + 65)
            elif ch.islower():
                decrypted += chr((ord(ch) - 97 - shift) % 26 + 97)
            else:
                decrypted += ch

        print("Decrypted Text:", decrypted)

    elif choice == 3:
        text = input("Enter encrypted string: ")

        print("\nPossible Decryptions:")
        for shift in range(26):
            decrypted = ""

            for ch in text:
                if ch.isupper():
                    decrypted += chr((ord(ch) - 65 - shift) % 26 + 65)
                elif ch.islower():
                    decrypted += chr((ord(ch) - 97 - shift) % 26 + 97)
                else:
                    decrypted += ch

            print(f"Shift {shift:2}: {decrypted}")

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please try again.")
