import re
I = 1
II = 2
III = 3
IV = 4
V = 5
VI = 6
X = 10
L = 50
C = 100
D = 500
M = 1000
# 100 = C


# 200 = CC
# 300 = CCC
# 400 = CD
# 500 = D
# 600 = DC
# 700 = DCC
# 800 = DCCC
# 900 = CM
pattern = '^M?M?M?(CM|CD|D?C?C?C?)$'
oo=re.search(pattern, 'MCM')
print(oo)
pattern1 = '^M{0,3}$'
m=re.search(pattern, 'M')
print(m)

# 校验十位数
pattern2 = '^M?M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)$'
pattern = '^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
re.search(pattern, 'MCMXL')
# 个位数的正则表达式
pattern = '^M?M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$'
