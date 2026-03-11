from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization
#Tools for locking + safety padding

with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read()) #read public key from file into python

with open("sample.txt", "rb") as file:
    data = file.read() #Read file content

encrypted = public_key.encrypt( #Locking start
    data, #Data to lock
    padding.OAEP( #Add safety layer
        mgf = padding.MGF1(algorithm = hashes.SHA256()),
        algorithm = hashes.SHA256(),
        label = None #Security math (don't change)
    )
)

with open("sample.txt", "wb") as file:
    file.write(encrypted) #Save locked data 

print("File encrypted using public key")