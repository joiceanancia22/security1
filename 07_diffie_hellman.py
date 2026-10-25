p = int(input("Enter Prime Number (p): "))
g = int(input("Enter Primitive Root (g): "))

alice_private = int(input("Enter Alice's Private Key: "))
bob_private = int(input("Enter Bob's Private Key: "))

alice_public = pow(g, alice_private, p)
bob_public = pow(g, bob_private, p)

alice_secret = pow(bob_public, alice_private, p)
bob_secret = pow(alice_public, bob_private, p)

print("\n----- OUTPUT -----")
print("Prime Number :", p)
print("Primitive Root :", g)
print("Alice's Private Key :", alice_private)
print("Bob's Private Key :", bob_private)
print("Alice's Public Key :", alice_public)
print("Bob's Public Key :", bob_public)
print("Alice's Shared Secret Key :", alice_secret)
print("Bob's Shared Secret Key :", bob_secret)

if alice_secret == bob_secret:
    print("Verification : Shared Keys are Identical")
else:
    print("Verification : Shared Keys are Different")
