# Απο python 3.7 η print κάνει insertion order για λόγους readibility
# στα dict. ΌΜΩς ΤΑ DICT ΔΕΝ ΕΙΝΑΙ ORDERED
new_dict = {'kiwi': 4, 'banana':2, 'apple':3, 'melon':1, 'orange':1}
new_dict['fig'] = 10

for key, value in new_dict.items():
  print(f"{key}:{value}", end=" ")
print()