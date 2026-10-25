import hashlib

while True:
    print("\n========== SHA-1 ==========")
    print("1. Generate SHA-1 Hash")
    print("2. Avalanche Effect")
    print("3. Compare Two Messages")
    print("4. SHA-1 Preprocessing")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        text = input("Enter text: ")

        if text == "":
            print("Text cannot be empty!")
        else:
            print("Original Message:", text)
            print("SHA-1 Hash:", hashlib.sha1(text.encode()).hexdigest())

    elif choice == "2":
        text = input("Enter original text: ")

        if text == "":
            print("Text cannot be empty!")
        else:
            pos = int(input("Enter position to change (1 to " + str(len(text)) + "): "))

            if pos < 1 or pos > len(text):
                print("Invalid position!")
            else:
                ch = input("Enter new character: ")

                if len(ch) != 1:
                    print("Enter only one character!")
                else:
                    modified = text[:pos - 1] + ch + text[pos:]

                    hash1 = hashlib.sha1(text.encode()).hexdigest()
                    hash2 = hashlib.sha1(modified.encode()).hexdigest()

                    print("\nOriginal Message:", text)
                    print("Original Hash:", hash1)
                    print("\nModified Message:", modified)
                    print("Modified Hash:", hash2)
                    print("Avalanche Effect:", "Hash values are different." if hash1 != hash2 else "Hash values are identical.")

    elif choice == "3":
        text1 = input("Enter first message: ")
        text2 = input("Enter second message: ")

        hash1 = hashlib.sha1(text1.encode()).hexdigest()
        hash2 = hashlib.sha1(text2.encode()).hexdigest()

        print("\nMessage 1 Hash:", hash1)
        print("Message 2 Hash:", hash2)

        if hash1 == hash2:
            print("Message digests are identical.")
        else:
            print("Message digests are different.")

    elif choice == "4":
        text = input("Enter a sentence: ")

        if text == "":
            print("Sentence cannot be empty!")
        else:
            binary = ""

            for c in text:
                binary += format(ord(c), "08b")

            print("\nOriginal Binary:")
            print(binary)

            length = len(binary)
            print("\nOriginal Length:", length, "bits")

            padded = binary + "1"

            while len(padded) % 512 != 448:
                padded += "0"

            padded += format(length, "064b")

            print("\nPadded Message:")
            print(padded)
            print("\nTotal Length:", len(padded), "bits")

            print("\n512-bit Blocks:")
            for i in range(0, len(padded), 512):
                print("\nBlock", i // 512 + 1)
                print(padded[i:i + 512])

            print("\nSHA-1 Message Digest:")
            print(hashlib.sha1(text.encode()).hexdigest())

    elif choice == "5":
        print("Program terminated.")
        break

    else:
        print("Invalid choice! Please try again.")
