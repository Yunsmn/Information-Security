from AES_decrypt import SBOX

# Encryption equation : c = S( S(p XOR k0) XOR k1 ) XOR k2
# From the first pair : k2 = S( S(p0 XOR k0) XOR k1 ) XOR c0

def Encrypt(p, k0, k1, k2):
    return SBOX[SBOX[p ^ k0] ^ k1] ^ k2

def Find_keys(pairs):
    p0, c0 = pairs[0]
    candidates = []

    for k0 in range(256):
        for k1 in range(256):
            k2 = SBOX[SBOX[p0 ^ k0] ^ k1] ^ c0
            if all(Encrypt(p, k0, k1, k2) == c for p, c in pairs):
                candidates.append((k0, k1, k2))

    return candidates

pairs = [(0x00, 0xA4), (0x01, 0xF8), (0x02, 0x3F)]

candidates = Find_keys(pairs)

print("Number of candidates : ", len(candidates))

print("=" * 50)

for k0, k1, k2 in candidates:
    print(f"k0 = {k0:02X}  k1 = {k1:02X}  k2 = {k2:02X}")
