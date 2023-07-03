# grid = [
#     [1, 2, 4 , 8],
#     [1, 3, 3 , 9]
# ]
#
# for i in zip(*grid):
#     print(*i[::-1])



strs = ["alic3","bob","3","4","00000"]
strs = ["1","01","001","0001"]
siz = float("-inf")
for i in range(len(strs)):
    if strs[i].isdigit() and len(strs[i]) > siz:
        siz = int(strs[i])
    elif strs[i].isalnum() and len(strs[i]) > siz:
        siz = len(strs[i])
print(siz)




