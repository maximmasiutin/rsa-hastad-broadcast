
# RSA Hastad Broadcast
Copyright (c) 2022 Maxim Masiutin

Copyright (c) 2018 Ashutosh Ahelleya

In 1988, Johan Hastad proposed a method to decrypt an RSA message without a private key,
if that same message was encrypted unmodified to several recipients,
and their keys have the same public exponent, such as 3 or 5.

The number of recipients should not be less than the value of the public exponent, i.e.,
with the exponent of 5, you need the same message to be encrypted to 5 different public keys.

This method was published as https://doi.org/10.1137/0217019
and it became known as Hastad's broadcast attack.

This Python 3 script can be used as a CTF (capture the flag) tool
to demonstrate this Hastad's broadcast attack.


## Version istory
### 2.0 (June 20, 2022)
- Ported to Python 3
### 1.0 (October 23, 2018)
- Initial revision from https://github.com/ashutosh1206/Crypton/tree/master/RSA-encryption/Attack-Hastad-Broadcast

## Usage

To use this software, modify the immediate values in `hastad-immval.py` and run this file which also serves as an example on how to use this attack
with the public exponent of 5 (5 encrypted messages): n1, n2, n3, n4 and n5 values are modulus; and the c1, c2, c3, c4 and c5 values are the ciphertexts.
