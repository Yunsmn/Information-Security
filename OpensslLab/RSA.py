p = 5
q = 11

n = p * q

e = 3

C = 23

def phi(p, q):
    return (p - 1) * (q - 1)

def private_key(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

def decrypt(C, d, n):
    return (C ** d) % n

phi_n = phi(p, q)
d = private_key(e, phi_n)
M = decrypt(C, d, n)

print("Private key (d) is:", d)

print("Decrypted message is:", M)

print('Checking if the decrypted message is correct: ', (M ** e) % n == C)

