def multiply_x(num1):
    def multiply_y(num2):
        return num1 * num2
    return multiply_y

def multiply_list_var1(liste:list, k:int):
    return list(map(lambda x: x * k, liste))

print(multiply_list_var1([1,2,3], 5))

def mutliply_list_var2(liste:list, k:int):
    mal_k = multiply_x(k)
    return list(map(mal_k, liste))

print(mutliply_list_var2([1,2,3], 5))
