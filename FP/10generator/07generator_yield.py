my_list = list(range(1,10))
print(my_list)

# Without Yield
def process_list(my_list):
    for i in range(len(my_list)):
        my_list[i] *= 2
    return my_list

print(process_list(my_list), end = ",")

# With Yield
def process_list_yield(my_list):
    for i in range(len(my_list)):
        my_list[i] *= 2
        yield my_list




