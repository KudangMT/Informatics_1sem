import sys

alph1 = "abcdefghijklmnopqrstuvwxyz"
alph2 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alph3 = "птхиёшцрыязэчджвфгмууюьоксещйбанл" # for monoalphabet. without frequency analasis but with trying to guess word and letters in cyphered text


def decode_atbash(text):
    output = ""
    for let in text:
        if let in alph1:
            output += alph1[25 - alph1.index(let)]
        if let in alph2:
            output += alph2[32 - alph2.index(let)]
        else:
            output += let
    return output


def decode_ceasar(text, key):
    output = ""
    for let in text:
        if let in alph1:
            output += alph1[(alph1.index(let)+key) % 26]
        if let in alph2:
            output += alph2[(alph2.index(let)+key) % 33]
        else:
            output += let
    return output


def decode_monoalphabet(text): # for rus only
    output = ""
    for let in text:
        if let in alph2:
            output += alph3[alph2.index(let)]
        else:
            output += let
    return output


def decode_vigenere(text, key):
    counter = 0
    output = ""
    length = len(key) - 1
    for let in text:
        if let in alph2:
            output += alph2[(alph2.index(let) + alph2.index(key[counter])) % 33]
        else:
            output += let
        counter += 1
        if counter > length:
            counter = 0
    return output

text = sys.stdin.readlines()
for line in text:
    print(decode_atbash(line.lower()))
    # print(decode_ceasar(line.lower(), 14))
    # print(decode_monoalphabet(line.lower()))
    # print(decode_vigenere(line.lower(), "мфти"))