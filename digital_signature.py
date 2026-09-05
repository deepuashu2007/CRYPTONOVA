from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey


# 1. Generate private key
private_key = Ed25519PrivateKey.generate()

# 2. Get public key
public_key = private_key.public_key()

# 3. Original document
document = b"Q-Sentinel Digital Signature Test"

# 4. Create digital signature
signature = private_key.sign(document)

print("Original Document:", document.decode())
print("Digital Signature Created Successfully!")
print("----------------------------------------")

# 5. Verify the signature
try:
    public_key.verify(signature, document)
    print("Signature Verification: VALID")
    print("Status: GENUINE")
except:
    print("Signature Verification: INVALID")
    print("Status: ATTACK / TAMPERED")