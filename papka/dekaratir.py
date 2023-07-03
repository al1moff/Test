# import json
#
# def digshner(dig):
#     def decc(j: dict):
#         if j["role"] == "ADMIN":
#             dig(j)
#     return decc
#
#
#
# @digshner
# def pechat(j: dict):
#     return j["username"]
#
# with open("file.json", 'r') as fil:
#     for rela in json.load(fil):
#         response = pechat(rela)
#         if response:
#             print(response)





# import json
#
#
# def decorator(func): # 4
#     def wrapper(user: dict): # 5
#         if user["role"] == "ADMIN": # 6
#             return func(user) # 7
#         # 7
#
#     return wrapper
#
#
# @decorator
# def print_user(user: dict): # 8
#     return user['username'] # 9
#
#
# with open("file.json" , 'r') as f: # 1
#     for user in json.load(f): # 2
#         response = print_user(user) # 3
#         if response:
#             print(response)





# def my_decorator(n1, n): # 3
#     def inner(func): # 4
#         def wrapper(n2): # 5
#             return n2[n1:n]
#         return wrapper
#     return inner
#
# @my_decorator(2, 8) # 2
# def multiple_num(num): # 7
#     return num # 8
#
# print(multiple_num("hello  world")) # 1
#




# def dekoratir(num, num1):
#     def number(func):
#         def string(str):
#             return func(str)[num:num1]
#         return string
#     return number
#
#
# @dekoratir(2, 5)
# def pechat(str):
#     return 1
#
# print(pechat("hello world"))




# def decoratir1(func: int):
#     def wrapper(num2: int):
#         return func(num2) * func
#     return wrapper
#
# def decoratir2(func: int):
#     def wrapper(num2: int):
#         return func(num2) * func
#     return wrapper
#
# @decoratir2(2)
# @decoratir1(3)
# def pechat(num: int):
#     return num
#
# print(pechat(10))


# def decoratir1(funk):
#     def decoratir2(func):
#         def decoratir3(*args):
#             return func(args) +
#         return decoratir3
#     return decoratir2
#
# @decoratir1(1, 2, 3)
#
# def pechat(num):
#     return num
#
# print(pechat(3))






# def massiv(num: list):
#     arr, sum = [], 0
#     for i in range(len(num)):
#         sum += num[i]
#         arr.append(sum)
#     return arr


# def massiv(num: list):
#     return [sum(num[:i+1]) for i in range(len(num))]
#
# aa = [1, 2, 3, 4, 5]
# print(massiv(aa))












