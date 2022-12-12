# Both functions do the same thing however map is a pure function as it does not have side effects to code outside of the function.


my_list = [2,9,61,41,37,21,7054,1.1,55.4]
def multiply_by2(item):
  return item * 2

print(list(map(multiply_by2, my_list)))


def multiply_by_2(list):
  new_list = []
  for item in list:
    new_list.append(item * 2)
  return new_list


print(multiply_by_2([3,6,10]))
    