code = input('Enter EAN-13 article number: ')
ok = isinstance(code, str) and len(code) == 13 and code.isdigit()
if ok:
    print('Article number is correct')
    if code.startswith('590'):
        print('Article manufactured in Poland')
else:
    print('Article number is incorrect')
