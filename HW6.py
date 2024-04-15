#1
# 입력: input(), read(), readline(), readlines()
# 출력: print(), write(), writeline()

#2
# Answer: 1

#3
# Answer: 1,3

#4

inFp = open("C:/Temp/data1.txt",'r")

inStr = inFp.readline()
print(inStr,end="")

inFp.writeline()

#6
inFp = open("C:/Windows/win.ini","r")
outFp = open("C:/Temp/data3.txt","w")

inList =inFp.readlines()
for inStr in inList :
    outFp.writelines(inStr)

inFp.close()
outFp.close()            

            
