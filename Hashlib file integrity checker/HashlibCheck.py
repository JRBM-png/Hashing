import hashlib 

CORRECT_HASH = "" #Input the hash you are expecting here, this is the hash of the file you are checking against

with open("", "rb")as f: #Input the exe. file you want to check here, this is the file you are checking against the hash

    file_bytes = f.read() #Reads the file as bytes, this is necessary for hashing the file, it will read the entire file and store it in memory

    h = hashlib.sha256() #This is the hashing algorithm, it takes an input and produces a fixed-size string of bytes, this is the same algorithm used to create the hash you are checking against, if you use a different algorithm, the hashes will not match

    h.update(file_bytes) #This is where the hashing happens, it takes the bytes of the file and updates the hash object with it, this is necessary for hashing the file, it will take the entire file and update the hash object with it, if you only update it with a portion of the file, the hash will not match
    
    file_hash = h.hexdigest() #This is where the hash is generated, it takes the hash object and generates a hexadecimal string representation of the hash, this is the format that is typically used for storing hashes, it is a string of characters that represents the hash, it is typically 64 characters long for sha256

print (file_hash == CORRECT_HASH)