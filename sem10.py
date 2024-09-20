import sys
import matplotlib.pyplot as plt
import numpy as np

alph1 = "abcdefghijklmnopqrstuvwxyz"
alph2 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alph3 = "птхиёшцрыязэчджвфгмууюьоксещйбанл"  # for monoalphabet. without frequency analasis but with trying to guess word and letters in cyphered text


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
            output += alph1[(alph1.index(let) + key) % 26]
        if let in alph2:
            output += alph2[(alph2.index(let) + key) % 33]
        else:
            output += let
    return output


def decode_monoalphabet(text):  # for rus only
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
            output += alph2[(alph2.index(let) - alph2.index(key[counter])) % 33]
            counter += 1
        else:
            output += let
        if counter > length:
            counter = 0
    return output


def frequency_analysis(text, period=1, shift=0):
    data = list(text)
    for let in text:
        if let in alph2:
            l = 0
        else:
            data.remove(let)
    print(data)
    new_data = data[shift::period]
    print(new_data)
    plt.hist(new_data, bins=66)
    plt.title('Histogram')
    plt.xlabel('Letter')
    plt.ylabel('Letters in text')
    plt.show()


text = sys.stdin.readlines()
# for line in text:
    # print(decode_atbash(line.lower()))
    # print(decode_ceasar(line.lower(), 14)) # 14 was found with cycle with changing key and one encoded word
    # print(decode_monoalphabet("".join(text).lower()))
# frequency_analysis("".join(text), 1) # for monoalphabet

key = "мфти"
print(decode_vigenere("".join(text), key))
# frequency_analysis(decode_vigenere("".join(text), key), 8, 2)
# alph2 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
# ыцящгнюзрвхщдз щгхья дбахжтыи дгч эщтфхьтяхт дфыыачпг вчшэтфбффсявблы мыээф -- эчщдожящгцат ячрщюе еэжщм "саспбн". ёшщянъжн хсжбмыц ксбебкмвыз, хёвчшръчоффбхйдз о бтбхвтю йжбт ющгсх, эдшыаоратеъл шб ъхй вчэ.
# промежуточный результат:
# иноарысйющеасх мегуо конииатш кре рыалегамиф слквнеге поздавфцвиоиощо оифмы -- кемёьюоардуф моаалт шяфрь "шняггы". эзамыниы мбноъош ширлошадия, емпелтзоюывоился ю заоидах щноа сырие, дсёовьзпщтзя ъо сер пер.