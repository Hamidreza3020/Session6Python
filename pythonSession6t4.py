numbers1 = [1, 2, 1, 4, 5, 5, 4]
numbers2 = [10, 2, 23, 54, 65, 87, 4]

unique_elements = []

for num in numbers1:
    if num  not in numbers2  and num not in unique_elements:
        unique_elements.append(num)
for num2 in numbers2:
    if num2 not in numbers1 and num not in unique_elements:
        unique_elements.append(num2)
    
print("مقادیر غیر مشترک:", unique_elements)