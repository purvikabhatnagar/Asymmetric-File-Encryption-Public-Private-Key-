from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization

with open("private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None
    ) #Load private key, Only this key can unlock

with open("sample.txt", "rb") as file:
    encrypted_data = file.read() #Read locked data

decrypted = private_key.decrypt( #Start unlocking
    encrypted_data,
    padding.OAEP( #Same padding as encryption (must be match)
        mgf = padding.MGF1(algorithm = hashes.SHA256()),
        algorithm = hashes.SHA256(),
        label = None #Same security settings
    )
)

with open("sample.txt", "wb") as file:
    file.write(decrypted) #Write original text back

print("File decrypted using private key")