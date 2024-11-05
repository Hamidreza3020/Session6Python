sentences = input(" Please inter sentences: ")

lisst = []
volwes = ['a','e','i','o','u']

for sen in sentences :
    if sen in volwes and sen not in lisst :
        lisst.append(sen)

print(f"lisst : {lisst}")