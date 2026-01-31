#1. Найдите ключ с минимальным значением в sample_dict = {'Physics': 82, 'Math': 65, 'history': 75}.
sample_dict = {'Physics': 82, 'Math': 80, 'history': 75}
min_num = min(sample_dict.values())
d = sample_dict.keys()
for i in d:
  if sample_dict.get(i) == min_num:
    print(f"Ключ с минимальным значением: {i}")
    break
