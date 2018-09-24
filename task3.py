def message(_string):
    _string = ' '.join(_string.title().strip().split())
    return _string


enter = str(input("Enter a string: "))
print (message(enter))
