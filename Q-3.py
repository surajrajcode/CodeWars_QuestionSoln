def alphabet_position(text):
    text = text.lower().strip()
    a = ''
    for i in text:
        if i.isalpha():
            a += str(ord(i) - 96) + ' '
    return a.strip()
        
    


print(alphabet_position('my name is suraj raj'))
