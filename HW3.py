# ex4

score = int(input("점수를 입력하세요 : "))

if score >= 90:
    print("장학생", end='')
elif score >= 60:
    print("합격", end='')
else:
    print("불합격", end='')

print("입니다.^^")

    
# ex5 answer: 3
num = 5
##1
#res = '홀수' if num %2 ==0 else '짝수'
##2
#res = if num %2 ==0 '짝수' else '홀수'
##3
res = '짝수' if num %2 ==0 else '홀수'
##4
#res if num $2 ==0 '홀수' else '짝수'

print(res)


#ex6


#1 answer: [100, 777, 300, 400, 500]
nn = [ 100,200,300,400,500 ]
nn[1] = 777
print('(1)', nn)

#2 answer:[100, [444, 555], 300, 400, 500]
nn = [100,200,300,400,500]
nn[1]=[444,555]
print('(2)',nn)
 
#3 answer: [100, 444, 555, 500]
nn = [100,200,300,400,500]
nn[1:4] = [444,555]
print('(3)',nn)

#4 answer: [100, 200]
nn = [100,200,300,400,500]
nn[2:]=[]
print('(4)',nn)


#ex9
hap = 0
for i in range(3333,10000):
    if i%1234 == 0:
        continue
        
    if hap+i > 100000:
        break
       
    hap += i       
    
    
print(hap)


#ex 8 answer: 23088
hap = 0
n = 1234

while n<4568:

    if n%444 ==0 :
        hap += n
    n +=1

print(hap)


#ex 14 answer: [[2, 4], [3, 6]]
myData = [[n*m for n in range(1,3)] for m in range(2,4)]
print(myData)


#ex 5

#1 answer: 500
nn = [100,200,300,400,500]
print('(1)',nn[4])

#2 answer: 500
nn = [100,200,300,400,500]
print('(2)',nn[-1])

#3 answer: 400
nn = [100,200,300,400,500]
print('(3)',nn[-2])

#4 answer: [200, 300, 400]
nn = [100,200,300,400,500]
print('(4)',nn[1:4])

#5 answer: [100]
nn = [100,200,300,400,500]
print('(5)',nn[0:1])

#6 answer: [300, 400]
nn = [100,200,300,400,500]
print('(6)',nn[2:-1])


#7 answer: [100, 300, 500]
nn = [100,200,300,400,500]
print('(7)',nn[0::2])

#8 answer: [500, 400, 300, 200, 100]
nn = [100,200,300,400,500]
print('(8)',nn[::-1])

