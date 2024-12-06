# Mini casse-tête ASCII

def decrypt(message: [int]) -> str:
    # Décrypte une liste de codes ASCII
    return ''.join(chr(num) for num in message)

if __name__ == '__main__':
    message = [84, 104, 105, 115, 32, 101, 120, 101, 114, 99, 105, 99,
               101, 32, 105, 115, 32, 97, 119, 101, 115, 111, 109, 101,
               32, 33]
    print(decrypt(message))
