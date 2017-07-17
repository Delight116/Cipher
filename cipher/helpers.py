import requests
from subprocess import Popen, PIPE

normal_alphabet = 'abcdefghijklmnopqrstuvwxyz'


def get_key_cipher(text):
    tuples = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
              'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, }
    for s in text:
        if normal_alphabet.rfind(s.lower()) and not s.isspace() and not s.isdigit():
            tuples[s.lower()] += 1

    return tuples


def searchKey(text):
    alphabets_key = []
    text_len = text.split(' ')
    print(text_len)
    for n in range(len(normal_alphabet)):
        for word in range(5):
                print(text_len[word])
                res = decrypt_texts(text_len[word], n)
                params_lang = {'text': res['text'], 'lang': 'en'}
                r = requests.get('http://speller.yandex.net/services/spellservice.json/checkText', params=params_lang)
                if r.status_code == 200 and len(r.json()) == 0:
                    alphabets_key.append({'key': n})
    key = 0
    results = 0

    for n in range(len(alphabets_key)):
        test = alphabets_key.count(alphabets_key[n])
        if results < test:
            results = test
            key = alphabets_key[n]['key']

    return key



def create_cipher_alphabet(key):
    cipher_alphabet = ''
    for n in range(len(normal_alphabet)):
        if (n + key) > len(normal_alphabet) - 1:
            cipher_alphabet += normal_alphabet[n + key - len(normal_alphabet)]
        else:
            cipher_alphabet += normal_alphabet[n + key]
    return cipher_alphabet


def encrypt_texts(text, key):

    encrypt_text = ''
    cipher_alphabet = create_cipher_alphabet(int(key))
    text_length = len(text)
    for n in range(text_length):
        if not text[n].isspace() and not text[n].isdigit():
            index_symbol = normal_alphabet.index(text[n].lower())
            encrypt_text += cipher_alphabet[index_symbol]
        else:
            if text[n].isspace():
                encrypt_text += ' '
            elif text[n].isdigit():
                encrypt_text += text[n]

    return encrypt_text


def decrypt_texts(encrypt_text, key):
    text_de_length = len(encrypt_text)
    decrypt_text = ''
    for n in range(text_de_length):
        if not encrypt_text[n].isspace() and not encrypt_text[n].isdigit():

            index_symbol = normal_alphabet.index(encrypt_text[n].lower())
            if (index_symbol - key) < 0:
                decrypt_text += normal_alphabet[index_symbol - key + len(normal_alphabet)]
            else:
                decrypt_text += normal_alphabet[index_symbol - key]

        else:
            if encrypt_text[n].isspace():
                decrypt_text += ' '
            elif encrypt_text[n].isdigit():
                decrypt_text += encrypt_text[n]

    return {'text': decrypt_text, 'key': key}
