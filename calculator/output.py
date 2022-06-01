def proverka(value):
    value = str(value)
    if '.' in value:
        value = float(value)
        x = round(value, 2)
        print(x)
    else:
        print(value)




