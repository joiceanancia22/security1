CRYPTOGRAPHY LAB PROGRAMS - ALGORITHM + IP/OP + VIVA
====================================================

Each Python program is separate. Sample outputs are representative; RSA/digital-signature outputs can change because keys/signatures are random.

1. HILL CIPHER - 01_hill_cipher.py
-----------------------------------
Algorithm:
1. Read plaintext and remove spaces.
2. Convert A=0...Z=25 and add X if length is odd.
3. Arrange values into a matrix.
4. Multiply by the key matrix modulo 26.
5. Convert the result to ciphertext.
6. Find determinant and modular inverse of the key.
7. Form inverse key matrix and multiply by ciphertext matrix.
8. Convert back to plaintext.

IP: Plaintext. Key is hardcoded as [[3,3],[2,5]].
Sample IP: HELLO
Sample OP: Ciphertext: HIOZQ (representative format); Decrypted Text: HELLO
Note: Exact matrix/ciphertext depends on the program's column arrangement.

Viva:
Q: What is Hill cipher? A: A matrix-based polygraphic substitution cipher.
Q: Why modulo 26? A: There are 26 English letters.
Q: Why must the key have an inverse? A: To decrypt the ciphertext.
Q: What is A? A=0, B=1, ..., Z=25.

Dependency: pip install numpy

2. PLAYFAIR CIPHER - 02_playfair_cipher.py
------------------------------------------
Algorithm:
1. Read keyword and plaintext; convert to uppercase and J to I.
2. Remove duplicate keyword letters.
3. Add remaining alphabet letters to form a 5x5 matrix.
4. Split plaintext into pairs; insert X between repeated letters and at the end if needed.
5. Same row: shift right. Same column: shift down. Rectangle: exchange columns.
6. Reverse the shifts for decryption.

IP: Keyword and plaintext.
Sample IP: Keyword=MONARCHY, Plaintext=INSTRUMENTS
Sample OP:
Key Matrix:
M O N A R
C H Y B D
E F G I K
L P Q S T
U V W X Z
Encrypted Text: GATLMZCLRQXA
Decrypted Text: INSTRUMENTSX

Viva:
Q: Why 5x5? A: 25 cells, so I/J are combined.
Q: Why X? A: To separate repeated letters and pad an incomplete pair.
Q: What happens to J? A: It is replaced by I.

Dependency: None

3. DIGITAL SIGNATURE USING RSA - 03_digital_signature_rsa.py
-------------------------------------------------------------
Algorithm:
1. Generate RSA private/public keys.
2. Hash the message using SHA-256.
3. Sign the hash with the private key.
4. Verify the signature with the public key.
5. Change the message to demonstrate failed verification.

IP: Menu choice and message.
Sample IP: Choice=2, Message=Hello
Sample OP: SHA-256 Hash=[64 hex chars]; Digital Signature=[Base64 value]; Message Signed Successfully!
Verification sample: Received message=Hello -> Signature Verification Successful!
Tampered sample: Hello hacked -> Verification Failed!

Viva:
Q: Which key signs? A: Private key.
Q: Which key verifies? A: Public key.
Q: Why SHA-256? A: It creates a fixed-size message digest before signing.
Q: Does a signature provide confidentiality? A: No; it mainly provides authenticity, integrity and non-repudiation.

Dependency: pip install pycryptodome

4. FILE INTEGRITY - 04_file_integrity.py
-----------------------------------------
Algorithm:
1. Load old checksums from checksums.json.
2. Read file names.
3. Calculate MD5 checksum for each existing file.
4. Compare with the stored checksum.
5. Report New File, Not Modified, Modified or Missing File.
6. Save the new checksums.

IP: File names separated by commas.
Sample IP: test.txt
Sample OP first run: test.txt : New File
Later unchanged: test.txt : Not Modified
After editing: test.txt : Modified

Viva:
Q: What is file integrity? A: Checking whether file contents changed.
Q: What is a checksum? A: A value calculated from data for comparison.
Q: Where is it stored? A: checksums.json.
Q: Why rb? A: To read the exact file bytes.

Dependency: None

5. MD5 MESSAGE DIGEST - 05_md5_message_digest.py
------------------------------------------------
Algorithm:
1. Read the selected operation.
2. Generate MD5 using hashlib.md5().
3. For verification, compare old and new digests.
4. For avalanche effect, compare hashes of different inputs.
5. For files, hash binary contents.
6. Optionally compare MD5, SHA-1 and SHA-256.

IP: Menu choice, text/digest/file path as required.
Sample IP: Choice=1, Text=HELLO
Sample OP: MD5 Digest: eb61eead90e3b899c6bcbe27ac581660

Viva:
Q: What is MD5? A: A 128-bit cryptographic hash function.
Q: Digest length? A: 32 hexadecimal characters.
Q: Is MD5 secure today? A: No, it has collision weaknesses.
Q: Can a hash normally be decrypted? A: No; hashing is designed to be one-way.

Dependency: None

6. SHA-1 - 06_sha1.py
----------------------
Algorithm:
1. Read message and convert it to binary.
2. Append 1, then zeros until length is 448 mod 512.
3. Append original length as 64 bits.
4. Process 512-bit blocks using SHA-1.
5. Output the SHA-1 digest.
6. For avalanche effect, change one character and compare hashes.

IP: Menu choice, text, position/new character or sentence.
Sample IP: Choice=1, Text=HELLO
Sample OP: Original Message: HELLO; SHA-1 Hash: [40 hex characters]

Viva:
Q: SHA-1 output size? A: 160 bits / 40 hexadecimal characters.
Q: Block size? A: 512 bits.
Q: Is SHA-1 secure today? A: No, it has practical collision weaknesses.
Q: What is padding? A: Adding bits and the original length to fit the block format.

Dependency: None

7. DIFFIE-HELLMAN - 07_diffie_hellman.py
-----------------------------------------
Algorithm:
1. Choose public prime p and primitive root g.
2. Alice chooses private a; Bob chooses private b.
3. A=g^a mod p; B=g^b mod p.
4. Alice computes S=B^a mod p.
5. Bob computes S=A^b mod p.
6. Compare the shared secrets.

IP: p, g, Alice private key, Bob private key.
Sample IP: p=23, g=5, Alice=6, Bob=15
Sample OP: Alice Public=8; Bob Public=19; Alice Shared=2; Bob Shared=2; Verification: Shared Keys are Identical

Viva:
Q: Purpose? A: Establish a shared secret over a public channel.
Q: Is it encryption? A: No, it is key exchange.
Q: Which values are private? A: Alice's and Bob's private keys.

Dependency: None

8. PLAYFAIR USING FUNCTIONS - 08_playfair_cipher_functions.py
---------------------------------------------------------------
Algorithm:
1. Generate a 5x5 matrix from the keyword.
2. Preprocess plaintext into pairs.
3. Find row/column positions using find_position().
4. Encrypt using Playfair rules.
5. Decrypt using reverse rules.

IP: Keyword and plaintext.
Sample IP: MONARCHY, INSTRUMENTS
Sample OP: Encrypted Text: GATLMZCLRQXA; Decrypted Text: INSTRUMENTSX

Viva:
Q: Why use functions? A: To divide the program into reusable modules.
Q: What does preprocess() do? A: Cleans text, replaces J, forms pairs and pads.
Q: What does find_position() return? A: Row and column of a character.

Dependency: None

9. RSA ENCRYPTION - 09_rsa_encryption.py
-----------------------------------------
Algorithm:
1. Generate a 2048-bit RSA key pair.
2. Encrypt plaintext using the public key and OAEP.
3. Display ciphertext as hexadecimal.
4. Decrypt using the private key.

IP: Plaintext.
Sample IP: HELLO
Sample OP: Ciphertext: [long hexadecimal value]; Decrypted Text: HELLO
Ciphertext changes between runs because OAEP uses randomization.

Viva:
Q: What is RSA? A: An asymmetric public-key cryptosystem.
Q: Which key encrypts here? A: Public key.
Q: Which key decrypts? A: Private key.
Q: What is OAEP? A: A secure padding scheme for RSA encryption.

Dependency: pip install pycryptodome

10. AES - 10_aes.py
-------------------
Algorithm:
1. Read plaintext and a 16-byte key.
2. Check key length.
3. Pad plaintext to 16-byte AES block size.
4. Encrypt using AES-ECB.
5. Decrypt and remove padding.
6. Display results.

IP: Plaintext and exactly 16-byte key.
Sample IP: Plaintext=HELLO, Key=1234567890123456
Sample OP: Plaintext=HELLO; Secret Key=1234567890123456; Ciphertext (Hex)=[hex value]; Decrypted Plaintext=HELLO

Viva:
Q: What is AES? A: A symmetric block cipher.
Q: Key size here? A: 128 bits / 16 bytes.
Q: AES block size? A: 128 bits / 16 bytes.
Q: What is ECB? A: Electronic Codebook mode.
Q: Is ECB recommended for real applications? A: No; authenticated modes such as GCM are generally preferred.

Dependency: pip install pycryptodome

11. COLUMNAR TRANSPOSITION - 11_columnar_transposition.py
----------------------------------------------------------
Algorithm:
1. Read plaintext and number of columns.
2. Remove spaces and add X padding.
3. Fill matrix column-wise.
4. Read row-wise to create ciphertext.
5. For decryption, fill row-wise and read column-wise.
6. Remove trailing X padding.

IP: Plaintext and number of columns.
Sample IP: HELLOWORLD, 3
Sample OP:
Encryption Matrix:
['H','L','O']
['E','L','R']
['L','O','D']
Ciphertext: HLOELRLOD
Decrypted Text: HELLOWORLD

Viva:
Q: What is transposition? A: Rearranging character positions without replacing the characters.
Q: Does it change letters? A: No, only their order.
Q: Why X? A: Padding.

Dependency: math

12. CAESAR CIPHER - 12_caesar_cipher.py
----------------------------------------
Algorithm:
1. Read operation, text and shift.
2. Encryption shifts letters forward.
3. Decryption shifts letters backward.
4. Modulo 26 provides wrap-around.
5. Brute force tries all 26 shifts.

IP: Menu choice, text and shift value.
Sample IP: Choice=1, Text=HELLO, Shift=3
Sample OP: Encrypted Cipher: KHOOR
Decryption sample: KHOOR, Shift=3 -> Decrypted Text: HELLO
Brute-force sample: Shift 3 -> HELLO

Viva:
Q: What is Caesar cipher? A: A substitution cipher using a fixed alphabet shift.
Q: What is the key? A: Shift value.
Q: Why modulo 26? A: 26 letters.
Q: Is it secure? A: No, only 26 shifts can be tried.
Q: What is brute force? A: Trying all possible keys until the plaintext is found.

Dependency: None

====================================================
COMMON VIVA QUESTIONS
====================================================
Q: What is plaintext? A: Original readable data.
Q: What is ciphertext? A: Encrypted data.
Q: What is encryption? A: Converting plaintext to ciphertext using an algorithm/key.
Q: What is decryption? A: Converting ciphertext back to plaintext.
Q: What is hashing? A: Converting data into a fixed-size digest.
Q: Hashing vs encryption? A: Encryption is reversible with a key; hashing is designed to be one-way.
Q: Symmetric vs asymmetric? A: Symmetric uses one shared secret key; asymmetric uses public/private keys.
Q: Examples of symmetric algorithms? A: AES and the classical ciphers in this lab.
Q: Example of asymmetric algorithm? A: RSA.
Q: What is integrity? A: Assurance that data was not modified.
Q: What is authentication? A: Verification of identity/authenticity.
Q: What is non-repudiation? A: Evidence that a signer cannot easily deny signing.
Q: What is avalanche effect? A: Small input changes cause a large output/hash change.
Q: Why are MD5 and SHA-1 not recommended? A: They have known collision/security weaknesses.
Q: Which is stronger among MD5, SHA-1 and SHA-256? A: SHA-256.

====================================================
INSTALLATION
====================================================
pip install numpy
pip install pycryptodome

Run examples:
python 01_hill_cipher.py
python 07_diffie_hellman.py
python 10_aes.py
python 12_caesar_cipher.py

NOTE:
MD5 and SHA-1 are retained for academic/lab purposes. They should not be used for modern security-sensitive applications.

============================================================
GENERAL CRYPTOGRAPHY THEORY VIVA QUESTIONS & ANSWERS
============================================================

1. What is Cryptography?
Answer: Cryptography is the technique of protecting information by converting readable data into an unreadable form and allowing only authorized users to access it.

2. What is plaintext?
Answer: Plaintext is the original readable message before encryption.

3. What is ciphertext?
Answer: Ciphertext is the encrypted, unreadable form of plaintext.

4. What is encryption?
Answer: Encryption converts plaintext into ciphertext using an algorithm and a key.

5. What is decryption?
Answer: Decryption converts ciphertext back into plaintext using a key and an algorithm.

6. What is a cryptographic key?
Answer: A key is a value used by a cryptographic algorithm to encrypt or decrypt data.

7. What are the main goals of cryptography?
Answer: The main goals are confidentiality, integrity, authentication, and non-repudiation.

8. What is confidentiality?
Answer: Confidentiality ensures that only authorized people can read the information.

9. What is integrity?
Answer: Integrity ensures that data has not been changed or tampered with without authorization.

10. What is authentication?
Answer: Authentication verifies the identity of a user, device, or system.

11. What is non-repudiation?
Answer: Non-repudiation provides proof that a sender performed an action or sent a message and cannot easily deny it later.

12. What is symmetric key cryptography?
Answer: Symmetric cryptography uses the same secret key for encryption and decryption.
Example: AES.

13. What is asymmetric key cryptography?
Answer: Asymmetric cryptography uses two related keys: a public key and a private key.
Example: RSA.

14. Difference between symmetric and asymmetric cryptography?
Answer: Symmetric cryptography uses one shared secret key and is generally faster. Asymmetric cryptography uses public and private keys and is generally slower but useful for secure key exchange and digital signatures.

15. What is a substitution cipher?
Answer: A substitution cipher replaces each character or group of characters with another character or group according to a rule.
Example: Caesar Cipher.

16. What is a transposition cipher?
Answer: A transposition cipher changes the positions of characters without changing the characters themselves.
Example: Columnar Transposition Cipher.

17. What is a block cipher?
Answer: A block cipher encrypts data in fixed-size blocks.
Example: AES.

18. What is a stream cipher?
Answer: A stream cipher encrypts data continuously, usually one bit or byte at a time.

19. What is a hash function?
Answer: A hash function converts input data of arbitrary length into a fixed-length hash value.

20. Is hashing encryption?
Answer: No. Hashing is a one-way process and is not designed to be decrypted like encryption.

21. What is a message digest?
Answer: A message digest is the fixed-length hash value generated from a message.

22. What is MD5?
Answer: MD5 is a hashing algorithm that produces a 128-bit message digest. It is useful for basic demonstrations and legacy checks, but it is not recommended for modern security because collision attacks exist.

23. What is SHA-1?
Answer: SHA-1 is a hashing algorithm that produces a 160-bit hash value. It is considered cryptographically weak for collision resistance and should not be used for new security applications.

24. What is SHA-256?
Answer: SHA-256 is a member of the SHA-2 family and produces a 256-bit hash value. It is widely used in modern security applications.

25. What is a collision in hashing?
Answer: A collision occurs when two different inputs produce the same hash value.

26. What is a digital signature?
Answer: A digital signature is a cryptographic mechanism used to verify the authenticity and integrity of a message and provide non-repudiation.

27. How does RSA digital signature work?
Answer: The sender hashes the message and signs the hash using the private key. The receiver uses the sender's public key to verify the signature and compares the resulting hash with the received message hash.

28. Why is hashing used before creating a digital signature?
Answer: Hashing creates a fixed-size digest, making the signing process faster and allowing the signature to represent the message efficiently.

29. What is RSA?
Answer: RSA is an asymmetric cryptographic algorithm based on the mathematical difficulty of factoring large integers.

30. What are public and private keys in RSA?
Answer: The public key can be shared openly and the private key must be kept secret. For encryption, the public key can encrypt and the private key decrypts. For signatures, the private key signs and the public key verifies.

31. What is OAEP in RSA?
Answer: OAEP stands for Optimal Asymmetric Encryption Padding. It adds randomized padding to RSA encryption and improves security against certain attacks.

32. Why is RSA not normally used to encrypt large files directly?
Answer: RSA is computationally slower and can only encrypt data within size limits related to the key size and padding. In practice, RSA is often used to protect a symmetric session key, while AES encrypts the actual data.

33. What is AES?
Answer: AES stands for Advanced Encryption Standard. It is a symmetric block cipher commonly used to protect data.

34. What are AES key sizes?
Answer: AES supports 128-bit, 192-bit, and 256-bit keys.

35. What is AES block size?
Answer: AES always uses a 128-bit block size, which is 16 bytes.

36. What is ECB mode?
Answer: ECB stands for Electronic Codebook. Each plaintext block is encrypted independently using the same key.

37. Why is ECB not recommended for real-world data?
Answer: Identical plaintext blocks produce identical ciphertext blocks, which can reveal patterns in the data. More secure modes such as GCM or CBC with proper IV handling are generally preferred.

38. What is a digital certificate?
Answer: A digital certificate binds an identity to a public key and is commonly issued by a Certificate Authority (CA).

39. What is a Certificate Authority?
Answer: A Certificate Authority is a trusted organization that issues and validates digital certificates.

40. What is Diffie-Hellman?
Answer: Diffie-Hellman is a key exchange method that allows two parties to establish a shared secret over an insecure communication channel.

41. Does Diffie-Hellman itself encrypt the message?
Answer: No. It establishes a shared secret key. A symmetric algorithm such as AES can then use that key for encryption.

42. What is a man-in-the-middle attack?
Answer: It is an attack in which an attacker secretly intercepts and possibly changes communication between two parties.

43. How can Diffie-Hellman be protected from a man-in-the-middle attack?
Answer: Diffie-Hellman should be authenticated, for example by using digital certificates or digital signatures.

44. What is the purpose of the modulo operation in cryptography?
Answer: Modular arithmetic keeps values within a defined range and is fundamental to algorithms such as RSA, Diffie-Hellman, and many classical ciphers.

45. Why is a key important in cryptography?
Answer: The algorithm may be publicly known, but the secret key controls access to the protected data. Keeping the key secret is critical for security.

46. What is brute-force attack?
Answer: A brute-force attack tries many possible keys or passwords until the correct one is found.

47. What is cryptanalysis?
Answer: Cryptanalysis is the study of analyzing cryptographic systems to discover weaknesses or recover protected information without knowing the secret key.

48. What is a cryptographic algorithm?
Answer: It is a mathematical procedure used to perform operations such as encryption, decryption, hashing, key exchange, or digital signing.

49. What is the difference between encoding and encryption?
Answer: Encoding changes data into another representation for storage or transmission and does not provide secrecy. Encryption is designed to protect confidentiality using a key.

50. What is the difference between hashing and encryption?
Answer: Encryption is reversible with the appropriate key, while hashing is intended to be one-way.

51. Which is faster: symmetric or asymmetric cryptography?
Answer: Symmetric cryptography is generally faster than asymmetric cryptography.

52. Why are both symmetric and asymmetric cryptography used together?
Answer: Asymmetric cryptography can securely establish or exchange a symmetric key, and symmetric cryptography can then efficiently encrypt large amounts of data.

53. What is a nonce or IV?
Answer: A nonce or initialization vector is an additional value used with certain encryption modes to make encryption safer and prevent repeated patterns. Its exact requirements depend on the algorithm and mode.

54. What is key management?
Answer: Key management includes generating, storing, distributing, rotating, using, and securely destroying cryptographic keys.

55. Why should private keys be protected?
Answer: Anyone who obtains a private key may be able to decrypt protected data or create valid digital signatures, depending on how the key is used.

56. Which algorithms in this lab are hashing algorithms?
Answer: MD5 and SHA-1 are hashing algorithms. The digital signature program also uses SHA-256 to create the message digest before signing.

57. Which algorithms in this lab are symmetric encryption algorithms?
Answer: AES, Caesar Cipher, Hill Cipher, Playfair Cipher, and Columnar Transposition are symmetric/classical cipher techniques because the same secret information or key is used by the communicating parties.

58. Which algorithms in this lab are asymmetric techniques?
Answer: RSA and Diffie-Hellman are asymmetric/public-key cryptographic techniques. RSA supports encryption and digital signatures, while Diffie-Hellman is primarily used for key exchange.

59. Why is MD5 still included in academic labs?
Answer: MD5 is useful for understanding message digests and file integrity concepts, even though it is not recommended for security-sensitive applications today.

60. Why are classical ciphers still studied?
Answer: Classical ciphers help students understand basic concepts such as substitution, transposition, keys, encryption, decryption, and cryptanalysis before learning modern cryptographic systems.

============================================================
QUICK COMPARISON FOR VIVA
============================================================

Caesar Cipher       -> Substitution cipher
Hill Cipher         -> Matrix-based substitution cipher
Playfair Cipher     -> Digraph substitution cipher
Columnar Transposition -> Transposition cipher
MD5                 -> 128-bit hash
SHA-1               -> 160-bit hash
SHA-256             -> 256-bit hash
AES                 -> Symmetric block cipher
RSA                 -> Asymmetric cryptosystem
Diffie-Hellman      -> Key exchange method
Digital Signature   -> Authentication + Integrity + Non-repudiation

============================================================
IMPORTANT VIVA ONE-LINERS
============================================================

- Plaintext = original readable data.
- Ciphertext = encrypted data.
- Encryption = plaintext to ciphertext.
- Decryption = ciphertext to plaintext.
- Hashing = one-way fixed-length digest generation.
- AES = symmetric encryption.
- RSA = asymmetric cryptography.
- Diffie-Hellman = shared-secret key exchange.
- MD5 = 128-bit hash, not recommended for modern security.
- SHA-1 = 160-bit hash, not recommended for new security applications.
- SHA-256 = 256-bit hash from the SHA-2 family.
- Digital signature = private-key signing and public-key verification.
- OAEP = secure padding scheme used with RSA encryption.
- Collision = two different inputs producing the same hash.
- Brute force = trying many possible keys until one works.
