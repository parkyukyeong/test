# ex1
print('ex1)')
print("100")
print(100)
print(50+50)
print("50+50")
print('Answer: 4')
print('--------------------------------------')

# ex2
print('ex2)')
print('%d / %d = %d' % (5,10,5/10))
print('Answer: 3')
print('--------------------------------------')

#ex3 
print('ex3)')
print("%04d" % 876)
print("%5s" % "CookBook")
print("%1.1f"% 123.45)
print('Answer: 1) 0876, 2) CookBook, 3) 123.5')
print('--------------------------------------')

#ex4
print('ex4)')
print("{2:d}{0:d}{1:d}".format(111,222,333))
print('Answer: 3')
print('--------------------------------------')

#ex11
print('ex11)')
a = int('1011',2)
print('a=',a)
b = int('1A',16)
print('b=',b)

print('Answer: 1) 11, 2) 26')

print('--------------------------------------')

#ex13
print('ex13)')
#int('1002',2) #>> Value error

#int('1008',8) >> Value error

#int('AAFG',16) >> Value error

print('Answer: 1) 2진법에는 2 존재하지 않음 2) 8진법에 8 존재하지 않음 3) 16진법에 G 존재하지 않음')

print('--------------------------------------')

#ex15, Answer: 아래와 같음
print('ex15)')
num = 12345678
hex_num = hex(num)
oct_num = oct(num)
bin_num = bin(num)
print("10진수==>",num)
print("16진수==>",hex_num)
print("8진수==>",oct_num)
print("2진수==>",bin_num)

print('Answer: hex_num = hex(num) ; oct_num = oct(num) ; bin_num = bin(num)')
