# Elliptic Curve Cryptography and Threshold Signature Scheme (TSS)

This repository demonstrates the key concepts of **Elliptic Curve Cryptography (ECC)** and how it integrates with **Threshold Signature Schemes (TSS)**. If you're new to ECC or TSS, this is a practical implementation designed to help you understand how these cryptographic techniques work under the hood.

## Overview

Elliptic Curve Cryptography (ECC) is a powerful cryptographic system that offers the same level of security as traditional systems like RSA but with much smaller key sizes. It's widely used for secure communications, key exchange, and digital signatures.

Threshold Signature Schemes (TSS) allow a group of participants to collaborate to generate a valid signature without any single participant having access to the full private key. This technique is highly useful in distributed systems, such as multi-signature wallets and secure voting systems.

## Key Features

- **Key Generation**: Generate ECC-based public and private key pairs.
- **Key Exchange**: Use Elliptic Curve Diffie-Hellman (ECDH) for secure key exchange.
- **Message Signing**: Sign a message using ECC-based digital signatures (ECDSA).
- **Signature Verification**: Verify the validity of a signature using the public key.

## How to Run

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/rosemary-crypto/ECC-TSS-Demo.git
   cd ECC-TSS-Demo
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Example**:

   ```bash
   python ecc_tss.py
   ```

## Elliptic Curve Cryptography (ECC)

- **Elliptic Curve Equation**: An elliptic curve is defined by the equation:

  \[
  y^2 = x^3 + ax + b
  \]

  where \(a\) and \(b\) are constants, and the curve is defined over a finite field for cryptographic purposes.

- **Key Operations**:
  - **Point Addition**: Adding two points on the elliptic curve to get another point.
  - **Scalar Multiplication**: Adding a point to itself multiple times to compute a scalar multiple of the point.

ECC is highly efficient and secure, making it a preferred choice in modern cryptographic applications.

## Simple ECC Implementation

For those who are interested in understanding the core mathematics behind Elliptic Curve Cryptography, we've included a basic implementation of elliptic curve operations such as point addition, point doubling, and scalar multiplication.

This implementation can be found in the `simple_ecc.py` file. Here, you can see how elliptic curve points are manipulated and multiplied, which forms the basis of ECC used in cryptography.

You can run this example as follows:

```bash
python simple_ecc.py
```

## Threshold Signature Scheme (TSS)

TSS allows a group of participants to generate a digital signature collaboratively without reconstructing the full private key. This technique is especially valuable in decentralized systems, such as multi-signature wallets in blockchain platforms.

## Further Reading

For a detailed explanation of ECC and how it powers TSS, check out the article accompanying this repository: [ECC and TSS Explained](https://rosemary-crypto.github.io/an-introduction-to-threshold-signature-schemes/).