import webbrowser

# this is the input string
string_in = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# a->c
# b->d
# .
# x->z
# y->a
# z->b

# function to perform simple decryption
def decrypt(message):
    string_out=''
    for character in message:
        ascii_character = ord(character)
        # only modify actual alphabetical characters
        if ascii_character < 97 or ascii_character > 122:
            string_out += character
            # special-case for wrap-around of y->a
        elif ascii_character == 121:
            string_out += 'a'
            # special-case for wrap-around of z->b
        elif ascii_character == 122:
            string_out += 'b'
            # otherwise follow the standard rule (2 letters after)
        else:
            string_out += chr(ascii_character+2)
    return string_out

print("Decrypting original message:")
print(decrypt(string_in))
print()
print("Decrypting original url and opening next page:")
target_url = 'http://www.pythonchallenge.com/pc/def/%s.html' % decrypt('map')
print(target_url)
webbrowser.open(target_url, new=2)

