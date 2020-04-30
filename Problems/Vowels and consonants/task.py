gl_ = ['a', 'e', 'i', 'o', 'u']
cons_ = ['q', 'w', 'r', 't', 'y', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']


list_text = list(str.lower(input()))
# print(list_text)
for char in list_text:
    # print(char)
    if char in gl_:
        print("vowel")
    elif char in cons_:
        print('consonant')
    else:
        break
