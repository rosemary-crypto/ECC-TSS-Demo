import secrets
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

def generate_key_pair():
    """
    Generates a public-private key pair using the NIST P-256 curve.
    """
    private_key = ec.generate_private_key(ec.SECP256R1())
    public_key = private_key.public_key()
    return private_key, public_key

def perform_key_exchange(private_key, peer_public_key):
    """
    Performs Elliptic Curve Diffie-Hellman (ECDH) key exchange.
    """
    shared_key = private_key.exchange(ec.ECDH(), peer_public_key)
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'handshake data',
    ).derive(shared_key)
    return derived_key

def sign_message(private_key, message):
    """
    Signs a message using the private key.
    """
    signature = private_key.sign(
        message,
        ec.ECDSA(hashes.SHA256())
    )
    return signature

def verify_signature(public_key, signature, message):
    """
    Verifies a signature using the public key.
    """
    try:
        public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
        return True
    except:
        return False

if __name__ == "__main__":
    # Generate key pairs for two parties
    alice_private, alice_public = generate_key_pair()
    bob_private, bob_public = generate_key_pair()

    # Perform Elliptic Curve Diffie-Hellman (ECDH) key exchange
    alice_derived_key = perform_key_exchange(alice_private, bob_public)
    bob_derived_key = perform_key_exchange(bob_private, alice_public)

    # Verify that both parties derived the same key
    if alice_derived_key == bob_derived_key:
        print("Key exchange successful! Both parties have the same shared secret.")
    else:
        print("Key exchange failed. The derived keys do not match.")

    print(f"\nShared secret (first 10 bytes): {alice_derived_key[:10].hex()}")

    # Sign and verify a message
    message = b"Hello, this is a test message."
    signature = sign_message(alice_private, message)
    print(f"Signature: {signature.hex()}")

    if verify_signature(alice_public, signature, message):
        print("Signature is valid.")
    else:
        print("Signature is invalid.")
