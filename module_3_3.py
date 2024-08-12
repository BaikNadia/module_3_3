def print_params (a = 1, b = 'string', c = True):
    print(a,b,c)

values_list = ['a', 10, False]
values_dict = {'a':18,'b':'string','c': False}
values_list_2 = [34, True]

print_params()
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)





