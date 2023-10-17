mas = [[10, 7, 4], [10, 7, 7], [1, 5, 9]]
mas_dict = {}

for i in range(len(mas)):
    avg = sum(mas[i]) / len(mas[i])
    mas_dict[f"mas{i}"] = mas[i]
    print(f"Середнє значення у масиві {i + 1}: {avg}")

sorted_dict = dict(sorted(mas_dict.items(), key=lambda item: sum(item[1]) / len(item[1])))

print("Масиви у порядку зростання їхніх середніх значень:", sorted_dict)