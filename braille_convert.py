braille_dict = {
    'a': '100000',
    'b': '101000',
    'c': '110000',
    'd': '110100',
    'e': '100100',
    'f': '111000',
    'g': '111100',
    'h': '101100',
    'i': '011000',
    'j': '011100',
    'k': '100010',
    'l': '101010',
    'm': '110010',
    'n': '110110',
    'o': '100110',
    'p': '111010',
    'q': '111110',
    'r': '101110',
    's': '011010',
    't': '011110',
    'u': '100011',
    'v': '101011',
    'w': '011101',
    'x': '110011',
    'y': '110111',
    'z': '100111',
    ' ': '000000',
    '1': '100000',
    '2': '101000',
    '3': '110000',
    '4': '110100',
    '5': '100100',
    '6': '111000',
    '7': '111100',
    '8': '100110',
    '9': '011000',
    '0': '110100',
    '.': '100101',
    ',': '100000',
    '-': '001000',
    '!': '001010',
    '?': '001110',
    ':': '001101',
    ';': '001001',
    '(': '001010',
    ')': '001010',
}

escapeCharacters = ['\n', '\r', '\t']

def convert_to_braille(text_to_convert):
    converted_text = ''

    for character in text_to_convert:
        if character in escapeCharacters:
            continue

        if character.isupper():
            character = character.lower()

        if character in braille_dict:
            converted_text  += braille_dict[character]
        else:
            converted_text += '000000'

    return converted_text
