# a = int(input("son kiriting: "))
# b = int(input("son kiriting: "))
#
# if a == b:
#     raise Exception("ikkalasi teng bo'lishi mumkin emas")
# if a > b:
#     print(a)
# else:
#     print(b)







# def num2word(m):
#     s1 = m // 100
#     s2 = (m // 10) % 10
#     s3 = m % 10
#
#     birlik = {
#         0: '',
#         1: 'bir',
#         2: 'ikki',
#         3: 'uch',
#         4: "to'rt",
#         5: 'besh',
#         6: 'olti',
#         7: 'yetti',
#         8: 'sakkiz',
#         9: "to'qqiz",
#     }
#     onlik = {
#         0: '',
#         1: "o'n",
#         2: "yigirma",
#         3: "o'ttiz",
#         4: "qirq",
#         5: "ellik",
#         6: "oltmish",
#         7: "yetmish",
#         8: "sakson",
#         9: "to'qson",
#     }
#     if s1 != 0:
#         son1 = birlik[s1] + 'yuz'
#     else:
#         son1 = ''
#     son2 = onlik[s2]
#     son3 = birlik[s3]
#     son = son1 + ' ' + son2 + ' ' + son3
#
#     return son.strip()
#
#
#
# nollar = {
#     1: 'ming',
#     2: 'million',
#     3: 'milliard',
#     4: 'trillion'
# }
# n = int(input("n= "))
# num = ''
# arr=[]
# while n > 0:
#     arr.append(n % 1000)
#     n //= 1000
#
# for i in range(1,len(arr)):
#     if arr[i] != 0:
#         num = num2word(arr[i]) + ' ' + nollar[i] + ' ' + num2word(arr[0])
# print(num.strip())




# def num3(son):
#     s1 = son // 100
#     s2 = (son // 10) % 10
#     s3 = son % 10
#
#     birlik = {
#         0: '',
#         1: 'bir',
#         2: 'ikki',
#         3: 'uch',
#         4: "to'rt",
#         5: 'besh',
#         6: 'olti',
#         7: 'yetti',
#         8: 'sakkiz',
#         9: "to'qqiz"
#     },
#     onlik = {
#         0: '',
#         2: 'yigirma',
#         3: "o'ttiz",
#         4: 'qirq',
#         5: 'ellik',
#         6: 'oltmish',
#         7: 'yetmish',
#         8: 'sakson',
#         9: "to'qson"
#     }
#     if s1 != 0:
#         son = birlik[s1] + 'yuz'
#     else:
#
#
#     arr=[]
#     while son > 0:
#         arr.append(son%1000)
#         son//=1000
#     return arr




class Harf_son:
    def __init__(self, son: int):
        self.son = son

    def birlik(self):
        s1 = self.son % 10
        bxona = {
            0: '',
            1: "bir",
            2: "ikki",
            3: "uch",
            4: "to'rt",
            5: "besh",
            6: "olti",
            7: "yetti",
            8: "sakkiz",
            9: "to'qqiz"
        }
        if self.son == 0:
            son1 = "nol"
        else:
            son1 = bxona[s1]
        return son1.strip()


    def onlik(self):
        s2 = self.son // 10 % 10
        oxona = {
            0: '',
            1: "o'n",
            2: "yigirma",
            3: "ottiz",
            4: "qirq",
            5: "ellik",
            6: "oltmish",
            7: "yetmish",
            8: "sakson",
            9: "to'qson"
        }
        son2 = oxona[s2]
        return son2.strip()


    def yuzlik(self):
        s3 = self.son // 100

        if s3 != 0:
            son3 = s3.birlik() + " yuz"
        else:
            son3 = ''
        return son3.strip()

    def pechat(self):
        return self.yuzlik() + ' ' + self.onlik() + ' ' + self.birlik()


sonlar = Harf_son(211)
print(sonlar.pechat())

