#!/usr/bin/env python3

txt = input("Enter text to encode\n")
key = input("Enter key\n")

def de_encode_word(txt, key, encode=1):
    ltrs = [
        None, 'a', 'b',
        'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z']

    output = ""
    for i, l in enumerate(txt):
        if l == " ":
            output += " "
        else:
            current = ""
            key_ltr = key[i % len(key)]
            key_ltr_num = ltrs.index(key_ltr)
            txt_ltr_num = ltrs.index(l)
            output_ltr_num = txt_ltr_num + key_ltr_num
            output_ltr = ltrs[
                output_ltr_num - 26
                if output_ltr_num > 26 else output_ltr_num]

        output += output_ltr
        current += (
            "key ltr num: %s - %s\n"
            "Plain ltr num: %s - %s\n"
            "Output: %s - %s\n\n") % (
            key_ltr, key_ltr_num,
            l, txt_ltr_num,
            output_ltr, output_ltr_num)

    return output

output = ""
for word in txt.split(" "):
    output += de_encode_word(word, key)
    output += " "
print(output)
