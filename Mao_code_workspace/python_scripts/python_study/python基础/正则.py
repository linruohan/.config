import re
s1 = '100 BROAD'

s = '100 BROAD ROAD APT. 3'
s0=re.sub('ROAD$','RD.',s)
s1=re.sub('\\bROAD$','RD.',s)
s2=re.sub(r'\bROAD$','RD.',s)
s3=re.sub(r'\bROAD\b','RD.',s)#only this is work
print(s0)
print(s1)
print(s2)
print(s3)