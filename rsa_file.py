import rsa

def encrypt_file_oaep(src_path: str, dest_path: str, public_key: rsa.Key ) :

    k = rsa.get_key_len(public_key)

    with open(src_path,'rb') as f:
        data = f.read()   

        with open(dest_path, 'wb') as g:

            for i in range(0,len(data), k-20*2-2):                   
                cipher_data=rsa.encrypt_oaep(data[i:i+k-20*2-2], public_key)
                g.write(cipher_data)


def decrypt_file_oaep(src_path: str, dest_path: str, private_key: rsa.Key ) :

    k = rsa.get_key_len(private_key)

    with open(src_path,'rb') as f:
        data = f.read()   

        with open(dest_path, 'wb') as g:
            
            for i in range(0,len(data), k):                   
                cipher_data=rsa.decrypt_oaep(data[i:i+k], private_key)
                g.write(cipher_data)


def encrypt_file_pkc1_v1_5(src_path: str, dest_path: str, public_key: rsa.Key ) :

    k = rsa.get_key_len(public_key)

    with open(src_path,'rb') as f:
        data = f.read()   

        with open(dest_path, 'wb') as g:

            for i in range(0,len(data), k-11):                   
                cipher_data=rsa.encrypt_v1_5(data[i:i+k-11], public_key)
                g.write(cipher_data)


def decrypt_file_pkc1_v1_5(src_path: str, dest_path: str, private_key: rsa.Key ) :

    k = rsa.get_key_len(private_key)

    with open(src_path,'rb') as f:
        data = f.read()   

        with open(dest_path, 'wb') as g:
            
            for i in range(0,len(data), k):                   
                cipher_data=rsa.decrypt_v1_5(data[i:i+k], private_key)
                g.write(cipher_data)
