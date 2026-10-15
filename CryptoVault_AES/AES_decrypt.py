# AES S-box (public standard table). For decryption, invert this mapping.
SBOX = [int(x, 16) for x in """63 7c 77 7b f2 6b 6f c5 30 01 67 2b fe d7 ab 76
ca 82 c9 7d fa 59 47 f0 ad d4 a2 af 9c a4 72 c0
b7 fd 93 26 36 3f f7 cc 34 a5 e5 f1 71 d8 31 15
04 c7 23 c3 18 96 05 9a 07 12 80 e2 eb 27 b2 75
09 83 2c 1a 1b 6e 5a a0 52 3b d6 b3 29 e3 2f 84
53 d1 00 ed 20 fc b1 5b 6a cb be 39 4a 4c 58 cf
d0 ef aa fb 43 4d 33 85 45 f9 02 7f 50 3c 9f a8
51 a3 40 8f 92 9d 38 f5 bc b6 da 21 10 ff f3 d2
cd 0c 13 ec 5f 97 44 17 c4 a7 7e 3d 64 5d 19 73
60 81 4f dc 22 2a 90 88 46 ee b8 14 de 5e 0b db
e0 32 3a 0a 49 06 24 5c c2 d3 ac 62 91 95 e4 79
e7 c8 37 6d 8d d5 4e a9 6c 56 f4 ea 65 7a ae 08
ba 78 25 2e 1c a6 b4 c6 e8 dd 74 1f 4b bd 8b 8a
70 3e b5 66 48 03 f6 0e 61 35 57 b9 86 c1 1d 9e
e1 f8 98 11 69 d9 8e 94 9b 1e 87 e9 ce 55 28 df
8c a1 89 0d bf e6 42 68 41 99 2d 0f b0 54 bb 16
""".split()]

INV_SBOX = [0] * 256
for index, value in enumerate(SBOX):
    INV_SBOX[value] = index

# First byte of each Rcon word, for the 10 AES-128 expansions.
RCON = [0x01, 0x02, 0x04, 0x08, 0x10,
        0x20, 0x40, 0x80, 0x1B, 0x36]


def expand_key(key):
    if len(key) != 16:
        raise ValueError("AES-128 requires exactly 16 key bytes")

    words = [list(key[4*i : 4*i+4]) for i in range(4)]

    for i in range(4, 44):
        temp = words[i-1].copy()
        if i % 4 == 0:
            temp = temp[1:] + temp[:1]          # RotWord
            temp = [SBOX[b] for b in temp]      # SubWord
            temp[0] ^= RCON[i//4-1]             # Rcon
        words.append([words[i-4][j] ^ temp[j] for j in range(4)])

    round_keys = []
    for rnd in range(11):
        cols = words[4*rnd : 4*rnd+4]
        round_keys.append([[cols[c][r] for c in range(4)] for r in range(4)])
    return round_keys


def bytes_to_state(block):
    # AES fills the state column by column
    return [[block[r + 4*c] for c in range(4)] for r in range(4)]


def state_to_bytes(state):
    return bytes(state[r][c] for c in range(4) for r in range(4))


def xtime(value):
    return ((value << 1) & 0xFF) ^ (0x1B if value & 0x80 else 0)


def add_round_key(state, round_key):
    for r in range(4):
        for c in range(4):
            state[r][c] ^= round_key[r][c]


def inv_shift_rows(state):
    for r in range(4):
        state[r] = state[r][-r:] + state[r][:-r]


def inv_sub_bytes(state):
    for r in range(4):
        for c in range(4):
            state[r][c] = INV_SBOX[state[r][c]]


def gf_mul(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        a = xtime(a)
        b >>= 1
    return result


INV_MIX_MATRIX = [[0x0e, 0x0b, 0x0d, 0x09],
                  [0x09, 0x0e, 0x0b, 0x0d],
                  [0x0d, 0x09, 0x0e, 0x0b],
                  [0x0b, 0x0d, 0x09, 0x0e]]


def inv_mix_columns(state):
    for c in range(4):
        column = [state[r][c] for r in range(4)]
        for r in range(4):
            value = 0
            for i in range(4):
                value ^= gf_mul(INV_MIX_MATRIX[r][i], column[i])
            state[r][c] = value


def decrypt_block(ciphertext, round_keys):
    state = bytes_to_state(ciphertext)

    add_round_key(state, round_keys[10])

    for rnd in range(9, 0, -1):
        inv_shift_rows(state)
        inv_sub_bytes(state)
        add_round_key(state, round_keys[rnd])
        inv_mix_columns(state)

    inv_shift_rows(state)
    inv_sub_bytes(state)
    add_round_key(state, round_keys[0])

    return state_to_bytes(state)


KEY = bytes.fromhex("2b7e151628aed2a6abf7158809cf4f3c")
CIPHERTEXT = bytes.fromhex("d21bb1d61866796323d61a23c635fb45")

if __name__ == "__main__":
    keys = expand_key(KEY)
    assert len(keys) == 11

    # Check InvMixColumns with the example of the appendix
    test = [[0x04], [0x66], [0x81], [0xe5]]
    test = [row * 4 for row in test]
    inv_mix_columns(test)
    print("InvMixColumns of 04 66 81 E5 : ", " ".join(f"{test[r][0]:02X}" for r in range(4)))

    print("=" * 50)

    plaintext = decrypt_block(CIPHERTEXT, keys)
    print("Plaintext (hex):", plaintext.hex())
    print("Secret message: ", plaintext.decode("ascii"))
