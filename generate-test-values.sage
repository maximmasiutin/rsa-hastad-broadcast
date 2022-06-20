# generate-test-values
# Copyright 2022 Maxim Masiutin
# This program is distributed under the MIT License
# See LICENSE for details


# This program is used to generate test values for hastad-immval.py
# Modify the values of "m", "bits" and "e" to suit your needs


from Crypto.Util.number import long_to_bytes, bytes_to_long


def encrypt(m, n, e):
    m = bytes_to_long(m)
    return pow(m, e, n)


m = "So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the".encode()
bits = 2048
e = 5
pn = 2 ^ (bits // 2) - 1
pl = 2 ^ (bits // 2 - 1)
for i in range(e):
    j = i + 1
    p = random_prime(pn, False, pl)
    q = random_prime(pn, False, pl)
    n = p * q
    print("n%d" % j, "=", n)
    c = encrypt(m, n, e)
    print("c%d" % j, "=", c)
