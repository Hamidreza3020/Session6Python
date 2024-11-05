numbers = [1, 2, 1, 4, 5, 5, 4]

listt = []

for num in numbers:
    if num not in listt:
        listt.append(num)

    
print(listt)