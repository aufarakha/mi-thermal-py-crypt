# mi-thermal-py-crypt
A python version of mi-thermal-crypt

Modify thermal configuration files (e.g., `thermal-normal.conf`) used by `mi-thermald` on Xiaomi, Redmi, and Poco devices. This tool allows you to decrypt configurations for editing and re-encrypt them for device compatibility, as `mi-thermald` only accepts encrypted files.

```
usage: thermal-crypt.py [-h] -i INFILE -o OUTFILE [-e]

Encrypt/decrypt mi_thermald configs

options:
  -h, --help            show this help message and
                        exit
  -i INFILE, --infile INFILE
                        Input filename
  -o OUTFILE, --outfile OUTFILE
                        Output filename
  -e, --encrypt         Encrypt input plain text file
                        to output file (default:
                        decrypt)
```

How to use:

Python Package
```
pip3 install cryptography 
```

Python Package (Termux)
```
apt install python-cryptography
```

Encrypt
```
python3 thermal-crypt.py -i decrypted.conf -o thermal-normal.conf -e
```

Decrypt
```
python3 thermal-crypt.py -i thermal-normal.conf -o decrypted.conf
```

<h1 align="center">Original Credit(C Version)</h1>
- [mi-thermal-crypt]
([https://github.com/adithya2306/mi-thermal-crypt])
