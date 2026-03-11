from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
#tools to make and save key
private_key = rsa.generate_private_key( #creating private key
    public_exponent = 65537, #standard safe number
    key_size = 2048 #key strength
)

public_key = private_key.public_key() #create public key from pvt key (Both are connected)

with open("private_key.pem", "wb") as f: #file to store pvt key
    f.write(
        private_key.private_bytes( #convert pvt key into file form
             encoding = serialization.Encoding.PEM, #key file format = normal text style
             format = serialization.PrivateFormat.TraditionalOpenSSL, #private key style (standard)
             encryption_algorithm = serialization.NoEncryption() #No password on key to keep simple
        )
    )

with open("public_key.pem", "wb") as f: #creating public key
    f.write( 
        public_key.public_bytes( #Converet oublic key into file form
            encoding = serialization.Encoding.PEM,
            format = serialization.PublicFormat.SubjectPublicKeyInfo #publci key format
        )
    )

print("Public and Private keys created")