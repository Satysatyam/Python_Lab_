my_tuple = (1, 2, 3, 4, 5)

print(my_tuple[0])

print(len(my_tuple))

print(my_tuple.count(3))

print(my_tuple.index(4))
#tuple using append
my_tuple = (1, 2, 3, 4, 5)

my_list = list(my_tuple)

my_list.append(2)

my_tuple = tuple(my_list)

print(my_tuple)