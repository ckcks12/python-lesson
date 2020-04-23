# 처음에 원하는 가격 출력
print(270000)

# 내 월급도 출력
print(400)

# 사칙연산
print(400 + 400) # 두달치모았을때
print(400 - 150) # 차할부냈을때
print(400*2) # 인센티브 탓을때
print(400 - (400 / 10)) # 십일조낼때

# 월급 더해서 얼마나걸리는지 볼까요
print(270000 - (400 + 400 + 400 + 400 + 400 + 400))

# 변수로 저장해서 써볼까요
price = 270000
salary = 400

price = price - salary
price = price - salary
price = price - salary
price = price - salary
price = price - salary

print(price) # 허걱 한참 남았네요



import random

apt = 27 * 100000000
print('내가 가지고 싶은 아파트는 27억입니다')
salary = float(input('연봉은?(?천만원) '))
salary = salary * 10000000
print('저축만으로는 ', apt/salary, '년 걸려요')
interest = 0.02
account = 0
year = 0
while account < apt:
    account += salary
    account += account * interest
    year += 1
print('은행 이자 복리 2% 로 하면 ', year, '년 걸려요')

account = 0
year = 0
for i in range(100):
    account += salary
    for j in range(12):
        account += random.randint(50 * 10000, 100 * 10000)
    year += 1
    if account >= apt:
        break
print('복권을 하게 되면 ', year, '년 걸려요')
