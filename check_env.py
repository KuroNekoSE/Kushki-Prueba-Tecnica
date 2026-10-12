import os
from dotenv import load_dotenv

load_dotenv()

public_key = os.getenv("KUSHKI_PUBLIC_KEY")
private_key = os.getenv("KUSHKI_PRIVATE_KEY")

print("Llave pública cargada:", bool(public_key))
print("Llave privada cargada:", bool(private_key))