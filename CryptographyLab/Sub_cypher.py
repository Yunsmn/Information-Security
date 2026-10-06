def Sub_cypher(text, sub):

    encrypted_text = ""
    for char in text:
        if char in sub:
            encrypted_text += sub[char]
        else:
            encrypted_text += char
    return encrypted_text


def Sub_decipher(text, sub):
    decrypted_text = ""
    reverse_sub = {v: k for k, v in sub.items()}
    for char in text:
        if char in reverse_sub:
            decrypted_text += reverse_sub[char]
        else:
            decrypted_text += char
    return decrypted_text

def Analyze(text) :
    frequency = {}
    sum = 0
    for char in text:
        if char.isalpha():
            char = char.upper()
            frequency[char] = frequency.get(char, 0) + 1
            sum += 1

    for freq in frequency:
        frequency[freq] = (frequency[freq] / sum) * 100

    return frequency


substitution = {
    'A': 'Q',
    'B': 'M',
    'C': 'J',
    'D': 'Z',
    'E': 'T',
    'F': 'G',
    'G': 'F',
    'H': 'K',
    'I': 'P',
    'J': 'W',
    'K': 'L',
    'L': 'S',
    'M': 'B',
    'N': 'O',
    'O': 'X',
    'P': 'N',
    'Q': 'C',
    'R': 'R',
    'S': 'Y',
    'T': 'E',
    'U': 'V',
    'V': 'H',
    'W': 'I',
    'X': 'A',
    'Y': 'D',
    'Z': 'U'
}

print("KEEP THE SECRET SAFE encrypted : ", Sub_cypher("KEEP THE SECRET SAFE", substitution))

print("="*50)

print("ERVYE DXVR SXFPJ decrypted : ", Sub_decipher("ERVYE DXVR SXFPJ", substitution))

print("="*50)

Analyzed_frequency = Analyze("EKT YTJRTE BTYYQFT PY KPZZTO PO EKPY NQRQFRQNK. STEETR GRTCVTOJD ZXTY OXE RTHTQS EKT IKXST LTD,MVE PE FPHTY Q FXXZ YEQRE.SXXL GXR JXBBXO IXRZY, RTNTQETZ NQEETROY,QOZ YKXRE IXRZY.IKTO DXV RTJXHTR EKT BTYYQFT,EKT HPFTOTRT LTD KQY GXVR STEETRY.")

print("Analyzed frequency of the text: ", sorted(Analyzed_frequency.items(), key=lambda x: x[1], reverse=True))

Substitution = {
    'T' : 'E',
    'H' : 'K',
    'E' : 'T',
    'A' : 'Q',
    'I' : 'P',
    'S' : 'Y',
    'N' : 'O',
    'C' : 'J',
    'R' : 'R',
    'D' : 'Z',
    'L' : 'S',
    'F' : 'G',
    'M' : 'B',
    'P' : 'N',
    'Q' : 'C',
    'U' : 'V',
    'O' : 'X',
    'W' : 'I',
    'Y' : 'D',
    'B' : 'M',
    'G' : 'F',
    'H' : 'K',
    'K' : 'L',
    'V' : 'H',
    'X' : 'A',
    'J' : '',
    'Z' : 'U'
}

print("="*50)

print("Decrypted text using the analyzed frequency: ", Sub_decipher("EKT YTJRTE BTYYQFT PY KPZZTO PO EKPY NQRQFRQNK. STEETR GRTCVTOJD ZXTY OXE RTHTQS EKT IKXST LTD,MVE PE FPHTY Q FXXZ YEQRE.SXXL GXR JXBBXO IXRZY, RTNTQETZ NQEETROY,QOZ YKXRE IXRZY.IKTO DXV RTJXHTR EKT BTYYQFT,EKT HPFTOTRT LTD KQY GXVR STEETRY.", Substitution))
