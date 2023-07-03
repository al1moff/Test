import datetime
import time
from datetime import date


#
# # now = datetime.datetime.now()
# date = input("sanani kiriting(dd.mm.yyyy): ")
# dte = datetime.datetime(*map(int, date.split('.')[::-1]))
#
# year = datetime.datetime(dte.year, 12, 31)
#
# print(year - dte)
#
# sec = 234352
# now = datetime.datetime.now()
# now = now.strftime("%Y-%m-%d")
# on = date.fromtimestamp(sec)
# # print(now - on)
# print(type(now),     '   ',  type(on))
#


# class Solution:
#     def __init__(self, operations: list):
#         self.operations = operations
#         x=0
#         for i in self.operations:
#             if i == '++X' or "X++":
#                 x += 1
#             else:
#                 x -= 1
#         print(x)
#
#
# Solution(['X++', '++X', '--X', "X--"])


# class Solution:
#     def __init__(self, op: str):
#         self.op = op
#         print(self.op.lower())
#
# Solution("Hello")
s = 'Salom alekum'
s = s.split()
d=''
for i in s:
    d += i[::-1]+' '

print(d)


























































































































































