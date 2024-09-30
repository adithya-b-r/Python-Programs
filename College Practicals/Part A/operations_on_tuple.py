t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

print(t1[:5])
print(t1[5:])

even_t1 = tuple(filter(lambda x: x % 2 == 0, t1))
print(even_t1)

t2 = (11, 13, 15)
concatenated_tuple = t1+t2

print(concatenated_tuple)
maximum = max(concatenated_tuple)
minimum = min(concatenated_tuple)

print("Maximum value : ", maximum)
print("Maximum value : ", minimum)