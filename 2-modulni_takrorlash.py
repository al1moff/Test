# def sum3(arr):
#     Max = max(arr[0], arr[2])
#     arr[0]=arr[1]=arr[2]=Max
#     return arr
#
# arr = [9, 2, 3]
# print(sum3(arr))



# def sum3(nums):
#     arr=[]
#     for i in nums:
#         arr.append(i)
#     return arr
#
# arr = [2, 4,3, 5, 3, 2, 4]
# arr = tuple(arr)
#
# print(arr)



git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/al1moff/Test.git
git push -u origin main

import re
#
# s = input("parol kiriting: ")
#
# # pattern = '[+]998(99|94)[0-9]{7}'
# pattern = '^([A-Z]*[a-z]+[A-Z]*[0-9]*[A-Z]*|[a-z]*[A-Z]+[a-z]*[0-9]*[a-z]*)@gmail.com'
# match = re.fullmatch(pattern, s)
# if match:
#     print('salom')
# else:
#     print('alik')

ss = input('parol kiriting: ')

pattern = "[a-zA-Z0-9]+@"

match = re.fullmatch(pattern, ss)

if match:
    print("salom")
else:
    print("alik")






























