
def Ceasar_cipher(text, shift):
    result = ""
    base = ord('A')

    for char in text:
        if char == ' ':
            result += ' '
        else:
            result += chr((ord(char) - base + shift) % 26 + base)

    return result

def Ceasar_decipher(text, shift):
    result = ""
    base = ord('A')

    for char in text:
        if char == ' ':
            result += ' '
        else:
            result += chr((ord(char) - base - shift) % 26 + base)

    return result

print("CRYPTO IS FUN UNTIL THE PROFESSOR SAYS QUIZ encrypted : ", Ceasar_cipher("CRYPTO IS FUN UNTIL THE PROFESSOR SAYS QUIZ", 4))

print("GWCL JMBBMZ VWB JM CAQVO BWWTA BW AWTDM BPQA decrypted : ", Ceasar_decipher("GWCL JMBBMZ VWB JM CAQVO BWWTA BW AWTDM BPQA", 8))

for i in range(1, 26):

    print(f"Shift {i}: {Ceasar_decipher('ESP VPJ TD FYVYZHY ECJ MCFEP QZCNP', i)}")