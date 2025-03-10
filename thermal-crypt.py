import argparse
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

def main():
    parser = argparse.ArgumentParser(description='Encrypt/decrypt mi_thermald configs')
    parser.add_argument('-i', '--infile', required=True, help='Input filename')
    parser.add_argument('-o', '--outfile', required=True, help='Output filename')
    parser.add_argument('-e', '--encrypt', action='store_true', 
                        help='Encrypt input plain text file to output file (default: decrypt)')
    args = parser.parse_args()

    # Key and IV (16 bytes each for AES-128-CBC)
    key = b'thermalopenssl.h'
    iv = b'thermalopenssl.h'

    with open(args.infile, 'rb') as f_in, open(args.outfile, 'wb') as f_out:
        if args.encrypt:
            # Read plaintext, pad, encrypt
            plaintext = f_in.read()
            padder = padding.PKCS7(128).padder()
            padded_data = padder.update(plaintext) + padder.finalize()
            
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            ciphertext = encryptor.update(padded_data) + encryptor.finalize()
            f_out.write(ciphertext)
        else:
            # Read ciphertext, decrypt, unpad
            ciphertext = f_in.read()
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
            
            unpadder = padding.PKCS7(128).unpadder()
            plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
            f_out.write(plaintext)

if __name__ == '__main__':
    main()