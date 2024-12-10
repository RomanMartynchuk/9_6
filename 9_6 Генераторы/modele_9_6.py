def all_variants(text):
    i = 0
    while i != len(text):
        yield text[i]
        i += 1
    i = 0
    x = 2
    while i != len(text)-1:
        yield text[i:x]
        i += 1
        x += 1
    yield text

a = all_variants("abc")
for i in a:
    print(i)



