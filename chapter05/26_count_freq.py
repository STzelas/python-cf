from collections import Counter

def count_with_dict_comprehension(my_list:list):
  frequency_dict = {item : my_list.count(item) for item in set(my_list)} # για να έχει τα uniques
  print(frequency_dict)

def count_with_manual_loop(my_list):
  frequency_dict = {}
  for item in my_list:
    if item in frequency_dict.keys():
      frequency_dict[item] += 1
    else:
      frequency_dict[item] = 1
  print(frequency_dict)

def count_with_get_method(my_list:list):
  frequency_dict = {}
  for item in my_list:
    frequency_dict[item] = frequency_dict.get(item, 0) + 1 # default = 0 επειδή είναι το πρώτο αντικείμενο άν δεν το βρει
  print(frequency_dict)

def count_with_counter(my_list):
  frequency_dict = Counter(my_list)
  sorted_frequency_dict = frequency_dict.most_common()
  print(sorted_frequency_dict)

def main():
  my_list = ["apple", "banana", "kiwi", "apple", "orange", "apple", "kiwi", "melon", "kiwi", "kiwi"]
  count_with_dict_comprehension(my_list)
  count_with_manual_loop(my_list)
  count_with_get_method(my_list)
  count_with_counter(my_list)

if __name__ == "__main__":
  main()