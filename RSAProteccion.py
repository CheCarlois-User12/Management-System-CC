from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

class RSAProteccion:
    def __init__(self):
        self.private_key = None
        self.public_key = None
        self.generate_keys()

    def generate_keys(self):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()

    def encrypt(self, message):
        return self.public_key.encrypt(
            message.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    def decrypt(self, encrypted_message):
        return self.private_key.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        ).decode()

    def save_keys(self, private_key_path, public_key_path):
        with open(private_key_path, 'wb') as private_file:
            private_file.write(
                self.private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()
                )
            )
        with open(public_key_path, 'wb') as public_file:
            public_file.write(
                self.public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                )
            )

    def load_keys(self, private_key_path, public_key_path):
        with open(private_key_path, 'rb') as private_file:
            self.private_key = serialization.load_pem_private_key(
                private_file.read(),
                password=None,
                backend=default_backend()
            )
        with open(public_key_path, 'rb') as public_file:
            self.public_key = serialization.load_pem_public_key(
                public_file.read(),
                backend=default_backend()
            )
if __name__ == '__main__':
    rsa_proteccion = RSAProteccion()
    rsa_proteccion.generate_keys()
    rsa_proteccion.save_keys('private_key.pem', 'public_key.pem')
