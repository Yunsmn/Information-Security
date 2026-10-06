from Sub_cypher import Analyze

def Vigenere_key_finder(text, key_len : int):
    groups = [text[i::key_len] for i in range(key_len)]
    frequencies = [Analyze(group) for group in groups]
    key = ""
    for feq in frequencies:
        most_common = max(feq, key=feq.get)
        shift = (ord(most_common) - ord('E')) % 26
        key += chr(shift + ord('A'))
    return key

def Vigenere_decipher(text, key):
    decrypted_text = ""
    key_length = len(key)
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % key_length]) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted_text += decrypted_char
            key_index += 1
        else:
            decrypted_text += char

    return decrypted_text

key =  Vigenere_key_finder("VVHWGQUIVYHIRSUPGTWXJSVIPCWIUPHGCIVIVVHPGHWITSDTRSDVUSYITMZLGFHIXSUCVSDQOSPFGFVLQIOHEVHGMSDGJQRPWAQWGSNXJSPSUHIVGEXIPHVCOPRPCBGYUSLXVCUIECYITHKIMSBAJSQXJSPIUGDKGPHGQAHWEZHETSQXGFWLGOFGGGVAQFGIEZLTUS", 4)
print("Key is : ", key)

print('=' * 50)

print("Decrypted text is : ", Vigenere_decipher("VVHWGQUIVYHIRSUPGTWXJSVIPCWIUPHGCIVIVVHPGHWITSDTRSDVUSYITMZLGFHIXSUCVSDQOSPFGFVLQIOHEVHGMSDGJQRPWAQWGSNXJSPSUHIVGEXIPHVCOPRPCBGYUSLXVCUIECYITHKIMSBAJSQXJSPIUGDKGPHGQAHWEZHETSQXGFWLGOFGGGVAQFGIEZLTUS", key))