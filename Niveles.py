def NivelFacil(vocales, secret_word):
    vocal = ''.join([char if char in vocales else '_' for char in secret_word])
    return vocal

def NivelMedio(secret_word):
    NM = secret_word[0] + "_" * (len(secret_word)-2) + secret_word[-1]
    return NM

def NivelDificil(secret_word):
    NM = "_" * len(secret_word)
    return NM