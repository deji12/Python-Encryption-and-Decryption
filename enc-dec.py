#importing module
from cryptography.fernet import Fernet

#generating key to be used for encryption and decryption
generated_key = Fernet.generate_key()

#saving generated key to a file because the generate_key() function will continue to generate random keys
save_key = open('key.key', 'wb').write(generated_key) #file is opened in wb mode because the key is in bytes

#open key file and assign to a variable
key = open('key.key', 'rb').read() #rb stands for read bytes

#a string we want to encrypt
#before encrypting, we need to encode it to make it suitable for encryption hence why you see .encode()
sentence = 'Subscribe to my youtube channel at THE PROTON GUY'.encode()
#note that you can also encrypt a file by opening it in read mode, encrypting all its contents, and rewriting the newly
#encrypted contents

#calling the fernet function on the key, we have:
f = Fernet(key)

#encrypting the string:
encrypted_sentence = f.encrypt(sentence)

#for decrypting string
decrypted_sentence = f.decrypt(encrypted_sentence)
#Now remember, you must not loose your key.  If you do, you will not be able to decrypt your file or string
#The end

