# Asymmetric File Encryption using Python

## Project Overview

This project demonstrates **asymmetric encryption** using a **public key and private key**.
In asymmetric encryption:
1. **Public Key** is used to encrypt the file
2. **Private Key** is used to decrypt the file

This method is commonly used in **secure communication and HTTPS**.

## Files in the Project

### `sample.txt`
The file that will be encrypted and decrypted.

### `keygen.py`
Generates two keys:

1. `public_key.pem`
2. `private_key.pem`

### `public_key.pem`
Used to encrypt files.

### `private_key.pem`
Used to decrypt files.

### `encrypt.py`
Uses the **public key** to encrypt the file.

### `decrypt.py`
Uses the **private key** to decrypt the file.

## How It Works

1. Run `keygen.py`
2. Public and private keys are created
3. `encrypt.py` uses the **public key** to encrypt the file
4. The file becomes unreadable
5. `decrypt.py` uses the **private key** to restore the file

## Installation

Install the required library:`
pip install cryptography


## Running the Project

Generate keys:
python keygen.py

Encrypt file:
python encrypt.py

Decrypt file:
python decrypt.py


## Important Notes
1. **Never share the private key**
2. Anyone can encrypt using the public key
3. Only the private key can decrypt the data

## Concept Learned
1. Asymmetric encryption
2. Public and private keys
3. RSA encryption
4. Secure file protection
