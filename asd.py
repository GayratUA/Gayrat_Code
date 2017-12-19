import random
str1 = '123456789'
str2 = 'qwertyuiopasdfghjklzxcvbnm'
str3 = str2.upper()
print(str3)

str4 = str1+str2+str3
print(str4)

ls = list(str4)
random.shuffle(ls)
psw = ''.join([random.choice(ls) for x in range(12)])
print(psw)
