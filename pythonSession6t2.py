numbers1 = [1, 2, 1, 4, 5, 5, 4]
numbers2 = [10, 2, 23, 54, 65, 87, 4]

listt = []

for num in numbers1:
    if num  in numbers2 and num not in listt:
        listt.append(num)

    
print(listt)